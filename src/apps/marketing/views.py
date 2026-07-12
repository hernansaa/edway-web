import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from .demo_data import generate_showcase_data
from .models import DemoRequest

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
"page_title": "Edway | CRM + Website + WhatsApp for Education Agencies",
"meta_description": "Edway is the all-in-one student recruitment platform. CRM, public website, WhatsApp automation, and custom development included. Save $450/month vs other CRMs with unlimited users.",
                "showcase": generate_showcase_data(),
                "hero_title": "The Student Recruitment CRM That Actually Works",
                "hero_subtitle": "Built by someone who used the most popular CRMs—and found them all lacking. Save $450/month with better features.",
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
                        "description": "$99/month unlimited users vs. $549/month for 5 users on other CRMs.",
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
"page_title": "Features | Edway — Complete Platform for Education Agencies",
"meta_description": "Explore all Edway features: lead management, intelligent quotations, invoicing, WhatsApp automation, email templates, public website builder, and custom development for education agencies.",
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
                                "description": "Handle school quotations and customized program quotations side by side — all within a single, unified system.",
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
                                "description": "Built-in WhatsApp messaging with automated templates triggered automatically on new enquiries.",
                            },
                            {
                                "title": "Email Template System",
                                "description": "Visual email editor with HTML support. Create templates with variables (student name, quotation details, etc.). Marketing team can edit without developer help.",
                            },
                            {
                                "title": "Background Task Processing",
                                "description": "Forms, emails, and WhatsApp messages process instantly in the background. Your team never waits — students get responses in seconds.",
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
                                "description": "A complete agency website included with your plan — mobile-responsive, SEO-optimized, and branded to you. Use it as your main site or keep your existing one. No pressure.",
                            },
                            {
                                "title": "Landing Page Builder",
                                "description": "Create landing pages for programs, destinations, or schools. Built-in lead capture forms with automatic CRM integration.",
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
                                "description": "Need a specific integration or workflow? We build custom features tailored to your agency's unique needs.",
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
    Pricing page with two plans: Professional and Enterprise.
    """

    template_name = "marketing/pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Pricing | Edway — From $89/Month",
                "meta_description": "Edway pricing starts at $89/month for 2 users. Professional CRM, public website, dedicated infrastructure, and custom development included. Flexible per-user pricing.",
                "plans": [
                    {
                        "name": "Professional",
                        "price_monthly": "$89",
                        "price_annual_first_year": "$44.50",
                        "price_annual_ongoing": "$71.20",
                        "annual_first_year_total": "$534",
                        "annual_ongoing_total": "$854",
                        "period": "per month",
                        "extra_user_monthly": "$39",
                        "extra_user_annual_first_year": "$19.50",
                        "extra_user_annual_ongoing": "$31.20",
                        "description": "Everything your agency needs to run and grow\u2014CRM, website, automation, and custom development.",
                        "features": [
                            "2 users included",
                            "Unlimited students & quotations",
                            "Full agency website included",
                            "Lead pipeline with 8 customizable stages",
                            "Multi-currency quotations",
                            "Invoice & payment tracking",
                            "WhatsApp automation",
                            "Email template system with variables",
                            "Blog with SEO optimization",
                            "Facebook lead ads integration",
                            "Executive dashboard with analytics",
                            "Multi-branch management",
                            "Daily automated backups",
                            "SSL certificate included",
                            "Custom development available as add-on",
                        ],
                        "cta": "Start free trial",
                        "cta_link": "/demo/",
                        "popular": True,
                        "badge": "Most popular",
                    },
                    {
                        "name": "Enterprise",
                        "price_monthly": None,
                        "price_annual_first_year": None,
                        "price_annual_ongoing": None,
                        "period": "Tailored to your scale",
                        "description": "Higher-tier dedicated infrastructure, priority support, and advanced capabilities for agencies managing significant volume.",
                        "features": [
                            "Dedicated server infrastructure",
                            "Everything in Professional",
                            "Higher-tier dedicated server resources",
                            "Unlimited users and team members",
                            "Priority support (4h response)",
                            "Dedicated account manager",
                            "Custom integrations & API access",
                            "Advanced reporting & analytics",
                            "Employee-specific SMTP configuration",
                            "Hourly automated backups",
                            "99.9% uptime SLA",
                            "Geographic deployment options",
                            "White-label options available",
                        ],
                        "cta": "Contact us",
                        "cta_link": "/demo/",
                        "popular": False,
                        "badge": None,
                    },
                ],
                "infrastructure_benefits": [
                    {
                        "title": "Dedicated server per agency",
                        "description": "Your data never shares resources with anyone else. Predictable performance, even during peak hours.",
                    },
                    {
                        "title": "Isolated email reputation",
                        "description": "Your own dedicated IP for email sending. No risk of deliverability issues from other tenants.",
                    },
                    {
                        "title": "Scale without migration",
                        "description": "Upgrade CPU, RAM, and storage on demand as your agency grows. No downtime, no data migration.",
                    },
                    {
                        "title": "Data sovereignty",
                        "description": "Host in your preferred region for compliance with local data protection regulations and lower latency.",
                    },
                ],
            },
        )
        return context


class WhyUsView(TemplateView):
    """
    Why choose Edway — built by agency operators, not just software developers.
    """

    template_name = "marketing/why_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "Why Us | Edway — The CRM Built for International Education Recruitment",
                "meta_description": "Built by agency operators with decades of experience. Edway gives you CRM, website, custom development, and dedicated infrastructure — all in one subscription.",
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
"page_title": "Request a Demo | Edway — See the CRM in Action",
"meta_description": "Request a personalized demo of Edway. See how the CRM, website builder, WhatsApp automation, and custom development work for your education agency in 30 minutes.",
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
"page_title": "Case Studies | Edway — Real Results from Education Agencies",
"meta_description": "Real results from education agencies using Edway. See how agencies increased conversions, automated WhatsApp, and saved money with the all-in-one recruitment platform.",
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
"page_title": "Documentation | Edway — Getting Started & API Reference",
"meta_description": "Complete Edway documentation: getting started guide, API reference, platform setup, and integration tutorials for education agencies using the CRM and website builder.",
            },
        )
        return context


class AboutView(TemplateView):
    """
    About page with founder story, team, and mission.
    """

    template_name = "marketing/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "page_title": "About | Edway — Built by Education Recruitment Experts",
                "meta_description": "Edway was built by people who ran international education agencies and tried every CRM on the market before building their own. Meet the team behind the platform.",
                "founder_story": {
                    "title": "Built by operators, not observers.",
                    "paragraphs": [
                        "We ran international education agencies for years before we wrote a single line of code. Every day, we saw how the available tools created friction instead of flow—so we decided to build something better.",
                        "Edway was born from the front lines of student recruitment. Not from a boardroom, not from investor demands, not from a product roadmap written by people guessing what agencies need. Every feature exists because we needed it ourselves.",
                        "Today, Edway is the platform we always wished we had—CRM, public website, automation, and custom development, all in one place. Built by operators, backed by real experience, and constantly improved based on what working agencies actually need.",
                    ],
                },
                "team": [
                    {
                        "name": "Hern\u00e1n Saavedra",
                        "role": "Founder & CEO",
                        "bio": "Years of experience running international education agencies across multiple continents. Built Edway from the ground up after growing frustrated with the limitations of existing platforms available to agencies. Leads product development and technical architecture, ensuring the platform solves real agency problems—not imaginary ones.",
                        "linkedin": "https://www.linkedin.com/in/hern%C3%A1n-saavedra-8144a9389/",
                        "initials": "HS",
                    },
                    {
                        "name": "Daniel Pastrana",
                        "role": "Head of Marketing & Growth",
                        "bio": "Leads Edway's go-to-market strategy, customer acquisition, and brand development. Brings deep understanding of the international education recruitment market and ensures Edway reaches the agencies that need a platform built by people who understand their work.",
                        "linkedin": "https://www.linkedin.com/in/dpastranabouchot/",
                        "initials": "DP",
                    },
                    {
                        "name": "Laura M\u00e9ndez",
                        "role": "Head of Customer Success",
                        "bio": "Ensures every agency that joins Edway gets onboarded, trained, and supported to their full potential. Previously managed student services for a multinational education group, giving her firsthand understanding of the workflows our customers run every day.",
                        "linkedin": "#",
                        "initials": "LM",
                    },
                    {
                        "name": "James Whitfield",
                        "role": "Head of Engineering",
                        "bio": "Leads the technical team responsible for platform reliability, performance, and continuous feature development. Background in building scalable SaaS infrastructure for regulated industries where uptime and data integrity are non-negotiable.",
                        "linkedin": "#",
                        "initials": "JW",
                    },
                    {
                        "name": "Sarah Mitchell",
                        "role": "Head of Operations",
                        "bio": "Oversees platform infrastructure, security, and compliance. Ensures Edway's dedicated servers, data protection practices, and operational processes meet the standards agencies and their students deserve.",
                        "linkedin": "#",
                        "initials": "SM",
                    },
                ],
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
"page_title": "Contact | Edway — Get in Touch with Our Team",
"meta_description": "Contact the Edway team. Reach us by email at info@edway.io, book a 30-minute call, or request a personalized demo of the student recruitment platform.",
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

            DemoRequest.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                message=message,
            )

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

                Thanks for your interest in Edway!

                We've received your demo request and will get back to you within 24 hours.

                In the meantime, feel free to explore our documentation at:
                https://edway.io/documentation/

                Best regards,
                Edway Team
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
