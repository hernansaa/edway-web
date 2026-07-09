import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .demo_data import generate_showcase_data

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    """
    Marketing homepage with hero, features overview, comparison, and CTAs.
    """

    template_name = "marketing/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Global Studies CRM - Modern Student Recruitment Software",
                "meta_description": "The most advanced student recruitment CRM built by industry experts. Save $450/month vs Edvisor with better features, WhatsApp automation, and instant performance.",
                "showcase": generate_showcase_data(),
                "hero_title": "The Student Recruitment CRM That Actually Works",
                "hero_subtitle": "Built by someone who used Edvisor, AMS4You, and Fidelo—and found them all lacking. Save $450/month with better features.",
                "key_features": [
                    {
                        "icon": "🎯",
                        "title": "Unified Lead Management",
                        "description": "All leads in one place. Facebook ads, landing pages, website forms—automatically captured and tracked.",
                    },
                    {
                        "icon": "⚡",
                        "title": "Lightning Fast",
                        "description": "95% faster than competitors. Form submissions in <100ms. No more waiting 5 seconds.",
                    },
                    {
                        "icon": "💬",
                        "title": "WhatsApp Automation",
                        "description": "Built-in WhatsApp with templates. Competitors charge $50/month extra or don't have it.",
                    },
                    {
                        "icon": "💰",
                        "title": "Save $450/Month",
                        "description": "$99/month unlimited users vs. $549/month for 5 users on Edvisor.",
                    },
                    {
                        "icon": "📧",
                        "title": "Smart Email Templates",
                        "description": "Marketing team edits templates without code. Competitors require developers.",
                    },
                    {
                        "icon": "🚀",
                        "title": "Modern Interface",
                        "description": "Beautiful, dark mode, mobile-responsive. Not stuck in 2010 like competitors.",
                    },
                ],
                "comparison_rows": [
                    {
                        "label": "Price / 5 users",
                        "edvisor": "$549/mo",
                        "ams4you": "€320/mo",
                        "sintra": "$99/mo",
                        "highlight": True,
                    },
                    {
                        "label": "WhatsApp",
                        "edvisor": "Not included",
                        "ams4you": "€50/mo extra",
                        "sintra": "Included",
                        "highlight": True,
                    },
                    {
                        "label": "Landing pages",
                        "edvisor": "Not available",
                        "ams4you": "Not available",
                        "sintra": "Included",
                        "highlight": True,
                    },
                    {
                        "label": "Facebook ads",
                        "edvisor": "Zapier required",
                        "ams4you": "Not available",
                        "sintra": "Native webhook",
                        "highlight": True,
                    },
                    {
                        "label": "Self-hosting",
                        "edvisor": "No",
                        "ams4you": "No",
                        "sintra": "Free",
                        "highlight": True,
                    },
                    {
                        "label": "Unlimited users",
                        "edvisor": "$50/seat",
                        "ams4you": "€30/seat",
                        "sintra": "Yes",
                        "highlight": True,
                    },
                ],
            },
        )
        return context


class FeaturesView(TemplateView):
    """
    Detailed features page with screenshots and technical details.
    """

    template_name = "marketing/features.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Features - Global Studies CRM",
                "meta_description": "Complete feature breakdown: Unified lead management, intelligent quotations, WhatsApp automation, email templates, background tasks, and more.",
                "feature_categories": [
                    {
                        "name": "Lead Management & CRM",
                        "icon": "🎯",
                        "features": [
                            {
                                "title": "8-Stage Lead Pipeline",
                                "description": "Complete lead workflow: New → Contacted → Qualified → Proposal Sent → Negotiation → Converted → Lost → Unresponsive. Track every lead from first contact to enrollment.",
                            },
                            {
                                "title": "Unified Contact Database",
                                "description": "All leads from landing pages, website forms, Facebook ads, and quote requests in one centralized system with complete history.",
                            },
                            {
                                "title": "Multi-Source Attribution",
                                "description": "Automatically track IP address, user agent, referrer URL, landing page, and campaign source for every lead. Know exactly where your students come from.",
                            },
                            {
                                "title": "Smart Lead Assignment",
                                "description": "Assign leads to employees or branches with automatic tracking of assignment date, first contact time, and next follow-up reminders.",
                            },
                            {
                                "title": "Complete Student History",
                                "description": "Full timeline from initial contact → quotation → invoice → payment → enrollment. Every interaction, email, and WhatsApp message in one place.",
                            },
                        ],
                    },
                    {
                        "name": "Quotation & Pricing",
                        "icon": "📋",
                        "features": [
                            {
                                "title": "Dual Quotation Types",
                                "description": "Support both COURSE quotations (language schools) and EXPERIENCE/PROGRAM quotations (work & study, internships) in one unified system.",
                            },
                            {
                                "title": "Automatic Seasonal Pricing",
                                "description": "Define high season and low season pricing. System automatically calculates total based on which weeks fall in each season—no manual calculations needed.",
                            },
                            {
                                "title": "Multi-Currency Support",
                                "description": "Store prices in school's local currency while displaying to clients in their preferred currency. Automatic exchange rate capture and conversion tracking.",
                            },
                            {
                                "title": "One-Click Approval Workflow",
                                "description": "Approve quotation → automatically creates invoice → automatically creates enrollment record. Complete automation from quote to enrollment.",
                            },
                            {
                                "title": "Comprehensive Pricing Components",
                                "description": "Course fees, accommodation, airport transfers, enrollment fees, materials—all itemized with automatic totals and calculations.",
                            },
                            {
                                "title": "Professional PDF Generation",
                                "description": "Branded quotation PDFs with itemized pricing, terms & conditions. Automatically attached to emails.",
                            },
                        ],
                    },
                    {
                        "name": "Invoicing & Payments",
                        "icon": "💰",
                        "features": [
                            {
                                "title": "Automated Invoice Creation",
                                "description": "Invoices generated automatically from approved quotations with unique invoice numbers, due dates, and payment tracking.",
                            },
                            {
                                "title": "Multi-Currency Transactions",
                                "description": "Accept payments in any currency with automatic exchange rate tracking. System converts to school's base currency for accounting.",
                            },
                            {
                                "title": "Payment Method Tracking",
                                "description": "Credit card, bank transfer, PayPal, cash, or custom methods. Track transaction fees, references, and attach receipt files.",
                            },
                            {
                                "title": "Enrollment Fee Management",
                                "description": "Separate tracking for enrollment fees with independent due dates. Automatic status updates (Paid, Due, Overdue).",
                            },
                            {
                                "title": "Outstanding Balance Tracking",
                                "description": "Real-time calculation of total paid vs. total due. Automatic payment status updates based on due dates and payment history.",
                            },
                            {
                                "title": "Refund Management",
                                "description": "Create refund invoices linked to original invoices. Track refund status and related transactions with complete audit trail.",
                            },
                        ],
                    },
                    {
                        "name": "Accounting & Finance",
                        "icon": "�",
                        "features": [
                            {
                                "title": "Provider Invoice Management",
                                "description": "Track invoices from schools and other providers. Link student invoices to provider invoices for complete financial visibility.",
                            },
                            {
                                "title": "Transaction Ledger",
                                "description": "Complete transaction history with IN/OUT tracking, exchange rates, and automatic school currency conversion for accurate accounting.",
                            },
                            {
                                "title": "Payment Status Automation",
                                "description": "Automatic status updates: Paid, Due, Overdue, Refunded. System monitors due dates and payment totals in real-time.",
                            },
                            {
                                "title": "Receipt Management",
                                "description": "Upload and attach receipt files to transactions. Organize all financial documents in one searchable system.",
                            },
                            {
                                "title": "Multi-Provider Support",
                                "description": "Manage invoices from schools, accommodation providers, insurance companies, and other service providers with separate tracking.",
                            },
                        ],
                    },
                    {
                        "name": "Communication & Automation",
                        "icon": "💬",
                        "features": [
                            {
                                "title": "WhatsApp Integration",
                                "description": "Built-in WhatsApp messaging with Twilio (paid) or Messagely (free self-hosted). Template-based messages with dynamic variables.",
                            },
                            {
                                "title": "Email Template System",
                                "description": "Visual email editor with HTML support. Create templates with variables (student name, quotation details, etc.). Marketing team can edit without developer help.",
                            },
                            {
                                "title": "Background Task Processing",
                                "description": "Emails and WhatsApp messages sent in background queue. Form submissions return in <100ms for instant user feedback. Production-ready with automatic retries.",
                            },
                            {
                                "title": "Automated Welcome Messages",
                                "description": "Configure automatic email + WhatsApp welcome messages per lead source. Instant response to new leads 24/7.",
                            },
                            {
                                "title": "Email Tracking & Logging",
                                "description": "Every email logged with timestamp, recipient, subject, and status. Complete audit trail of all communications.",
                            },
                            {
                                "title": "Employee-Specific SMTP",
                                "description": "Each employee can send emails from their own email address. Configurable SMTP settings per user for personalized communication.",
                            },
                        ],
                    },
                    {
                        "name": "Website & Marketing",
                        "icon": "🌐",
                        "features": [
                            {
                                "title": "Professional Agency Website",
                                "description": "Complete public-facing website included. Modern design, mobile-responsive, SEO-optimized. Your domain, your branding.",
                            },
                            {
                                "title": "Landing Page Builder",
                                "description": "Create unlimited landing pages for programs, destinations, or schools. Built-in lead capture forms with automatic CRM integration.",
                            },
                            {
                                "title": "Blog System with SEO",
                                "description": "Full-featured blog with categories, tags, featured images, and SEO meta fields. Share student stories, destination guides, and agency news.",
                            },
                            {
                                "title": "Facebook Lead Ads Integration",
                                "description": "Native webhook integration—Facebook leads appear in CRM instantly. No third-party tools needed.",
                            },
                            {
                                "title": "Lead Capture Forms",
                                "description": "Contact forms, quote request forms, and custom forms. All submissions automatically create leads in CRM with source attribution.",
                            },
                            {
                                "title": "View & Conversion Tracking",
                                "description": "Track page views and form submissions per landing page. Measure conversion rates and optimize your marketing.",
                            },
                        ],
                    },
                    {
                        "name": "Enrollment & Student Management",
                        "icon": "🎓",
                        "features": [
                            {
                                "title": "Automatic Enrollment Creation",
                                "description": "Enrollments created automatically when quotations are approved or when enrollment fee is paid. No manual data entry.",
                            },
                            {
                                "title": "Enrollment Status Tracking",
                                "description": "Real-time status: Enrolled (fully paid), Pending (partial payment), Cancelled. Automatic updates based on payment status.",
                            },
                            {
                                "title": "Program Date Management",
                                "description": "Track course start/finish dates and accommodation dates separately. Automatic date calculations for program duration.",
                            },
                            {
                                "title": "Student Profile System",
                                "description": "Complete student profiles with contact info, date of birth, status, assigned branch, and assigned employee.",
                            },
                            {
                                "title": "Multi-Branch Support",
                                "description": "Manage multiple agency branches with separate student assignments, employee access, and performance tracking.",
                            },
                        ],
                    },
                    {
                        "name": "Reporting & Analytics",
                        "icon": "�",
                        "features": [
                            {
                                "title": "Executive Dashboard",
                                "description": "Real-time metrics with date range filtering. Lead distribution, conversion rates, financial health, and team performance at a glance.",
                            },
                            {
                                "title": "Employee-Specific Views",
                                "description": "Each employee sees their own dashboard with assigned leads, quotations, enrollments, and performance metrics.",
                            },
                            {
                                "title": "Financial Reports",
                                "description": "Revenue tracking, outstanding balances, payment status breakdowns, and transaction history with multi-currency support.",
                            },
                            {
                                "title": "Lead Source Analytics",
                                "description": "Track which marketing channels generate the most leads and enrollments. ROI analysis per source.",
                            },
                            {
                                "title": "Complete Audit Trail",
                                "description": "Every action logged with timestamp and user: emails sent, status changes, payments received, quotations created.",
                            },
                        ],
                    },
                    {
                        "name": "Custom Development",
                        "icon": "⚙️",
                        "features": [
                            {
                                "title": "Custom Feature Development",
                                "description": "Need a specific integration or workflow? We build custom features tailored to your agency's needs—included in your subscription.",
                            },
                            {
                                "title": "API Integrations",
                                "description": "Connect to external systems: payment gateways, accounting software, marketing tools. We handle the technical integration.",
                            },
                            {
                                "title": "Custom Reports",
                                "description": "Need specific metrics or data exports? We create custom reports and dashboards based on your requirements.",
                            },
                            {
                                "title": "Workflow Automation",
                                "description": "Automate repetitive tasks specific to your agency. Custom email triggers, status updates, and notification rules.",
                            },
                            {
                                "title": "Ongoing Platform Evolution",
                                "description": "Your feedback shapes the platform. We continuously add features and improvements based on real agency needs.",
                            },
                        ],
                    },
                ],
            },
        )
        return context


class PricingView(TemplateView):
    """
    Pricing page with comparison to competitors.
    """

    template_name = "marketing/pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Pricing — Sintra CRM",
                "meta_description": "Premium dedicated infrastructure. From $299/month with unlimited users. Enterprise-grade performance without enterprise complexity.",
                "plans": [
                    {
                        "name": "Professional",
                        "price": "$299",
                        "price_annual": "$2,990",
                        "period": "per month",
                        "period_annual": "per year",
                        "setup_fee": "$499",
                        "setup_fee_waived": True,
                        "savings_annual": "$598",
                        "description": "Dedicated server instance. Perfect for agencies managing 50-200 students per month.",
                        "features": [
                            "Dedicated server (4 vCPU, 8GB RAM)",
                            "Unlimited users & team members",
                            "Unlimited students & quotations",
                            "Full agency website included",
                            "Blog system with SEO optimization",
                            "Complete student history tracking",
                            "Lead management & pipeline (8 statuses)",
                            "Multi-currency quotation system",
                            "Invoice & payment tracking",
                            "WhatsApp automation (Twilio/Messagely)",
                            "Email template system with variables",
                            "Landing page builder (unlimited)",
                            "Facebook lead ads webhook integration",
                            "Executive dashboard with analytics",
                            "Multi-branch management",
                            "Daily automated backups",
                            "SSL certificate included",
                            "99.5% uptime SLA",
                            "Email support (24h response)",
                            "Onboarding & migration assistance",
                        ],
                        "cta": "Start 30-day trial",
                        "cta_link": "#demo",
                        "popular": False,
                        "badge": None,
                    },
                    {
                        "name": "Business",
                        "price": "$599",
                        "price_annual": "$5,990",
                        "period": "per month",
                        "period_annual": "per year",
                        "setup_fee": "$499",
                        "setup_fee_waived": True,
                        "savings_annual": "$1,198",
                        "description": "High-performance dedicated infrastructure. For agencies managing 200-500 students per month.",
                        "features": [
                            "Dedicated server (8 vCPU, 16GB RAM)",
                            "Unlimited users & team members",
                            "Unlimited students & quotations",
                            "Full agency website included",
                            "Blog system with SEO optimization",
                            "Complete student history tracking",
                            "Lead management & pipeline (8 statuses)",
                            "Multi-currency quotation system",
                            "Invoice & payment tracking",
                            "Accounting module with transactions",
                            "WhatsApp automation (Twilio/Messagely)",
                            "Email template system with variables",
                            "Landing page builder (unlimited)",
                            "Facebook lead ads webhook integration",
                            "Executive dashboard with analytics",
                            "Multi-branch management",
                            "Employee-specific SMTP configuration",
                            "Email client with compose & tracking",
                            "Hourly automated backups",
                            "SSL certificate included",
                            "99.9% uptime SLA",
                            "Priority support (4h response)",
                            "Dedicated account manager",
                            "Custom integrations (API support)",
                            "Advanced reporting & analytics",
                        ],
                        "cta": "Start 30-day trial",
                        "cta_link": "#demo",
                        "popular": True,
                        "badge": "Most popular",
                    },
                    {
                        "name": "Enterprise",
                        "price": "$1,199",
                        "price_annual": "$11,990",
                        "period": "per month",
                        "period_annual": "per year",
                        "setup_fee": "$499",
                        "setup_fee_waived": True,
                        "savings_annual": "$2,398",
                        "description": "Maximum performance and scalability. For networks managing 500+ students per month.",
                        "features": [
                            "Dedicated server (16 vCPU, 32GB RAM)",
                            "Unlimited users & team members",
                            "Unlimited students & quotations",
                            "Full agency website included",
                            "Blog system with SEO optimization",
                            "Complete student history tracking",
                            "Lead management & pipeline (8 statuses)",
                            "Multi-currency quotation system",
                            "Invoice & payment tracking",
                            "Accounting module with transactions",
                            "WhatsApp automation (Twilio/Messagely)",
                            "Email template system with variables",
                            "Landing page builder (unlimited)",
                            "Facebook lead ads webhook integration",
                            "Executive dashboard with analytics",
                            "Multi-branch & multi-location support",
                            "Employee-specific SMTP configuration",
                            "Email client with compose & tracking",
                            "Newsletter management system",
                            "Course & experience program management",
                            "Real-time backups & replication",
                            "SSL certificate included",
                            "99.95% uptime SLA",
                            "Premium support (1h response)",
                            "Dedicated account manager",
                            "Custom integrations & API",
                            "Advanced reporting & analytics",
                            "White-label options available",
                        ],
                        "cta": "Contact sales",
                        "cta_link": "#demo",
                        "popular": False,
                        "badge": "Maximum scale",
                    },
                ],
                "competitor_comparison": [
                    {
                        "name": "Edvisor.io",
                        "base_price": "$299/month",
                        "per_user": "$50/user",
                        "total_5_users": "$549/month",
                        "infrastructure": "Shared multi-tenant",
                        "performance": "Variable (shared)",
                    },
                    {
                        "name": "AMS4You",
                        "base_price": "€200/month",
                        "per_user": "€30/user",
                        "total_5_users": "€320/month",
                        "infrastructure": "Shared multi-tenant",
                        "performance": "Variable (shared)",
                    },
                    {
                        "name": "Fidelo",
                        "base_price": "$150/month",
                        "per_user": "$25/user",
                        "total_5_users": "$275/month",
                        "infrastructure": "Shared multi-tenant",
                        "performance": "Variable (shared)",
                    },
                    {
                        "name": "Sintra (Business)",
                        "base_price": "$599/month",
                        "per_user": "Unlimited",
                        "total_5_users": "$599/month",
                        "infrastructure": "Dedicated server",
                        "performance": "Guaranteed (isolated)",
                    },
                ],
                "infrastructure_benefits": [
                    {
                        "title": "Dedicated server per client",
                        "description": "Your data never shares resources. Predictable performance, even during peak hours.",
                    },
                    {
                        "title": "Isolated email sending",
                        "description": "Your own IP reputation. No risk of deliverability issues from other tenants' spam.",
                    },
                    {
                        "title": "Scalable on demand",
                        "description": "Upgrade CPU/RAM instantly as your agency grows. No migration, no downtime.",
                    },
                    {
                        "title": "Geographic deployment",
                        "description": "Host in your region for GDPR compliance and lower latency for your team.",
                    },
                ],
            },
        )
        return context


class ComparisonView(TemplateView):
    """
    Detailed side-by-side comparison with competitors.
    """

    template_name = "marketing/comparison.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Sintra vs Edvisor, AMS4You, Fidelo — Full Comparison",
                "meta_description": "Honest feature-by-feature comparison. See why agencies switch from Edvisor, AMS4You, and Fidelo to Sintra.",
                "comparison_table": [
                    # Core Offering
                    {
                        "feature": "What's included",
                        "edvisor": "CRM only",
                        "ams4you": "CRM only",
                        "fidelo": "CRM only",
                        "sintra": "CRM + Website + Custom Dev",
                    },
                    {
                        "feature": "Public website included",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ Full agency website",
                    },
                    {
                        "feature": "Custom feature development",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ Included in subscription",
                    },
                    {
                        "feature": "Dedicated server",
                        "edvisor": "Shared",
                        "ams4you": "Shared",
                        "fidelo": "Shared",
                        "sintra": "✓ 100% dedicated",
                    },
                    # Pricing
                    {
                        "feature": "Starting price/month",
                        "edvisor": "~$549",
                        "ams4you": "~€320",
                        "fidelo": "~$275",
                        "sintra": "$299",
                    },
                    {
                        "feature": "User limits",
                        "edvisor": "Per seat pricing",
                        "ams4you": "Per seat pricing",
                        "fidelo": "Per seat pricing",
                        "sintra": "✓ Unlimited",
                    },
                    {
                        "feature": "Student/quotation limits",
                        "edvisor": "Varies by plan",
                        "ams4you": "Varies by plan",
                        "fidelo": "Varies by plan",
                        "sintra": "✓ Unlimited",
                    },
                    # Website & Marketing
                    {
                        "feature": "Landing page builder",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ Unlimited pages",
                    },
                    {
                        "feature": "Blog system with SEO",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ Full CMS",
                    },
                    {
                        "feature": "Facebook lead ads integration",
                        "edvisor": "Via Zapier",
                        "ams4you": "Limited",
                        "fidelo": "Via Zapier",
                        "sintra": "✓ Native webhook",
                    },
                    {
                        "feature": "Custom domain & SSL",
                        "edvisor": "N/A",
                        "ams4you": "N/A",
                        "fidelo": "N/A",
                        "sintra": "✓ Included",
                    },
                    # CRM Features
                    {
                        "feature": "Lead pipeline stages",
                        "edvisor": "Basic",
                        "ams4you": "3 stages",
                        "fidelo": "Basic",
                        "sintra": "✓ 8 customizable stages",
                    },
                    {
                        "feature": "Complete student history",
                        "edvisor": "✓",
                        "ams4you": "✓",
                        "fidelo": "✓",
                        "sintra": "✓ Contact→Quote→Invoice→Enrollment",
                    },
                    {
                        "feature": "Multi-currency quotations",
                        "edvisor": "Limited",
                        "ams4you": "Limited",
                        "fidelo": "Basic",
                        "sintra": "✓ Full exchange rate tracking",
                    },
                    {
                        "feature": "Course + Experience programs",
                        "edvisor": "Courses only",
                        "ams4you": "Courses only",
                        "fidelo": "Courses only",
                        "sintra": "✓ Both types",
                    },
                    # Communication
                    {
                        "feature": "WhatsApp automation",
                        "edvisor": "✗",
                        "ams4you": "Extra cost",
                        "fidelo": "✗",
                        "sintra": "✓ Twilio + Messagely",
                    },
                    {
                        "feature": "Email template system",
                        "edvisor": "Basic",
                        "ams4you": "Basic",
                        "fidelo": "Basic",
                        "sintra": "✓ Full HTML + variables",
                    },
                    {
                        "feature": "Background task processing",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ <100ms response",
                    },
                    # Technical
                    {
                        "feature": "API for integrations",
                        "edvisor": "Limited",
                        "ams4you": "Limited",
                        "fidelo": "Limited",
                        "sintra": "✓ Full REST API",
                    },
                    {
                        "feature": "Self-hosting option",
                        "edvisor": "✗",
                        "ams4you": "✗",
                        "fidelo": "✗",
                        "sintra": "✓ Open source available",
                    },
                    {
                        "feature": "Multi-branch support",
                        "edvisor": "✓",
                        "ams4you": "✓",
                        "fidelo": "Limited",
                        "sintra": "✓ Unlimited branches",
                    },
                ],
            },
        )
        return context


class DemoView(TemplateView):
    """
    Demo page with video and interactive tour.
    """

    template_name = "marketing/demo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Demo - See Global Studies CRM in Action",
                "meta_description": "Watch a video demo or request a personalized demo with our team.",
            },
        )
        return context


class CaseStudiesView(TemplateView):
    """
    Success stories from agencies using the system.
    """

    template_name = "marketing/case_studies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Case Studies - Global Studies CRM",
                "meta_description": "See how agencies increased conversions and saved money with Global Studies CRM.",
            },
        )
        return context


class DocumentationView(TemplateView):
    """
    Getting started guide and documentation.
    """

    template_name = "marketing/documentation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Documentation - Global Studies CRM",
                "meta_description": "Complete documentation, API reference, and getting started guide.",
            },
        )
        return context


class AboutView(TemplateView):
    """
    About page with founder story and mission.
    """

    template_name = "marketing/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "About - Global Studies CRM",
                "meta_description": "Built by industry experts who actually used the competitors and found them lacking.",
                "founder_story": {
                    "title": "Built by Someone Who Actually Used the Competitors",
                    "paragraphs": [
                        "I spent years using Edvisor, AMS4You, and Fidelo. Each one frustrated me in different ways.",
                        "Edvisor was expensive and slow. AMS4You was rigid and outdated. Fidelo was basic and limited.",
                        "So I built Global Studies CRM—the system I wish existed when I started.",
                        "Every feature solves a real problem. Every optimization came from actual pain points.",
                        "This isn't just another CRM. It's the evolution of student recruitment software.",
                    ],
                },
            },
        )
        return context


class ContactView(TemplateView):
    """
    Contact page with form.
    """

    template_name = "marketing/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Contact - Global Studies CRM",
                "meta_description": "Get in touch with our team. We're here to help.",
            },
        )
        return context


class RequestDemoView(View):
    """
    Handle demo request form submissions.
    """

    def post(self, request):
        try:
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            company = request.POST.get("company", "")
            phone = request.POST.get("phone", "")
            message = request.POST.get("message", "")

            # Send notification email to sales team
            send_mail(
                subject=f"Demo Request from {name} ({company})",
                message=f"""
                New demo request:

                Name: {name}
                Email: {email}
                Company: {company}
                Phone: {phone}
                Message: {message}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Send confirmation email to requester
            send_mail(
                subject="Thanks for requesting a demo!",
                message=f"""
                Hi {name},

                Thanks for your interest in Global Studies CRM!

                We've received your demo request and will get back to you within 24 hours.

                In the meantime, feel free to explore our documentation at:
                https://globalstudiescrm.com/documentation/

                Best regards,
                Global Studies CRM Team
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(
                request,
                "Thanks for requesting a demo! We'll be in touch within 24 hours.",
            )
            logger.info(f"Demo request from {email} ({company})")

        except Exception as e:
            logger.error(f"Error processing demo request: {e}", exc_info=True)
            messages.error(
                request,
                "Sorry, there was an error processing your request. Please try again or email us directly.",
            )

        return redirect("marketing:demo")
