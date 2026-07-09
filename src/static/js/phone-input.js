/**
 * International Phone Input — Professional Edition
 *
 * Production-grade telephone input handler with:
 * - Multi-service geoIP country detection (3 services + browser locale fallback)
 * - Session-cached detection results
 * - E.164 formatting on form submission
 * - Opt-in strict validation (landing pages block invalid numbers)
 * - Automatic initialization via data-phone-input attribute
 *
 * Usage:
 *   <input type="tel" id="my_field" data-phone-input>
 *
 *   // On form submit:
 *   validateAndConvertPhoneOnSubmit('my_field', event, true); // strict
 */

const GEOLOCATION_SERVICES = [
  { url: 'https://ipapi.co/json/', transform: d => d.country_code },
  { url: 'https://ip-api.com/json/?fields=countryCode', transform: d => d.countryCode },
  { url: 'https://ipinfo.io/json', transform: d => d.country },
];

const LOCALE_COUNTRY_MAP = {
  en: 'US', es: 'ES', pt: 'BR', fr: 'FR', de: 'DE', it: 'IT',
  ja: 'JP', zh: 'CN', ko: 'KR', ru: 'RU', ar: 'SA',
  nl: 'NL', pl: 'PL', sv: 'SE', no: 'NO', fi: 'FI', da: 'DK',
  cs: 'CZ', hu: 'HU', ro: 'RO', uk: 'UA', el: 'GR', he: 'IL',
  hi: 'IN', bn: 'BD', th: 'TH', vi: 'VN', tr: 'TR',
};

function getCountryFromLocale() {
  try {
    const lang = (navigator.language || navigator.languages?.[0] || '').toLowerCase();
    const parts = lang.split('-');
    if (parts.length >= 2 && parts[1].length === 2) return parts[1].toUpperCase();
    return LOCALE_COUNTRY_MAP[parts[0]] || null;
  } catch { return null; }
}

function tryGeoIPService(index, callback) {
  if (index >= GEOLOCATION_SERVICES.length) { callback(null); return; }
  const service = GEOLOCATION_SERVICES[index];
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 4000);
  fetch(service.url, { signal: controller.signal })
    .then(r => r.json())
    .then(data => {
      clearTimeout(timer);
      const code = service.transform(data);
      if (code && /^[A-Z]{2}$/i.test(code)) { callback(code.toUpperCase()); }
      else { tryGeoIPService(index + 1, callback); }
    })
    .catch(() => { clearTimeout(timer); tryGeoIPService(index + 1, callback); });
}

window.resolveUserCountry = function(callback) {
  const cached = sessionStorage.getItem('iti_user_country');
  if (cached) { callback(cached); return; }

  const locale = getCountryFromLocale();
  if (locale) {
    sessionStorage.setItem('iti_user_country', locale);
    callback(locale);
    return;
  }

  tryGeoIPService(0, function(code) {
    if (code) sessionStorage.setItem('iti_user_country', code);
    callback(code || null);
  });
};

function initPhoneInput(inputId, options) {
  var phoneInput = document.querySelector('#' + inputId);
  if (!phoneInput) return null;

  var config = {
    initialCountry: 'auto',
    geoIpLookup: function(callback) {
      window.resolveUserCountry(function(code) {
        callback(code || 'us');
      });
    },
    utilsScript: '/static/vendor/intl-tel-input/js/utils.js',
    separateDialCode: true,
    preferredCountries: ['ar', 'br', 'co', 'mx', 'es', 'us', 'gb', 'ie', 'au', 'ca'],
    autoPlaceholder: 'aggressive',
    formatOnDisplay: true,
    nationalMode: false,
  };

  if (options) {
    for (var key in options) {
      if (options.hasOwnProperty(key)) config[key] = options[key];
    }
  }

  var iti = window.intlTelInput(phoneInput, config);
  phoneInput.itiInstance = iti;
  return iti;
}

function validateAndConvertPhoneOnSubmit(inputId, event, strictValidation) {
  var phoneInput = document.querySelector('#' + inputId);
  if (!phoneInput || !phoneInput.itiInstance) return true;

  var iti = phoneInput.itiInstance;

  if (phoneInput.value.trim()) {
    if (strictValidation && !iti.isValidNumber()) {
      if (event) event.preventDefault();
      alert('Please enter a valid phone number');
      phoneInput.focus();
      return false;
    }
    try {
      var fullNumber = iti.getNumber();
      if (fullNumber) phoneInput.value = fullNumber;
    } catch (e) {}
  }
  return true;
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('[data-phone-input]').forEach(function(input) {
    if (input.id) initPhoneInput(input.id);
  });
});
