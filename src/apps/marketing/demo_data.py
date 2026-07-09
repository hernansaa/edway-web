"""
Demo data generators for the marketing site showcase.
Generates realistic fake CRM data mirroring the actual system models.
"""

from dataclasses import dataclass, field


@dataclass
class DemoLead:
    name: str
    country: str
    program: str
    source: str
    stage: str
    assigned_to: str
    age: int
    time_ago: str
    flag: str  # emoji flag
    quotation_amount: str | None = None
    quotation_status: str | None = None
    days_in_stage: int = 0


@dataclass
class DemoDashboardMetric:
    label: str
    value: str
    change: str  # e.g. "+12%"
    change_type: str  # "up" or "down"
    icon: str  # SVG path


@dataclass
class DemoQuotation:
    id: str
    student: str
    destination: str
    program: str
    amount: str
    currency: str
    status: str  # draft, sent, approved, rejected
    date: str
    weeks: int


@dataclass
class DemoInvoice:
    id: str
    student: str
    amount: str
    status: str  # paid, due, overdue
    due_date: str
    paid_amount: str


@dataclass
class DemoActivity:
    action: str
    detail: str
    time: str
    type: str  # lead, quotation, invoice, enrollment, email


@dataclass
class DemoEnrollment:
    student: str
    program: str
    start_date: str
    status: str  # enrolled, pending, cancelled
    amount: str


@dataclass
class DemoShowcaseData:
    pipeline_stages: dict[str, list[DemoLead]] = field(default_factory=dict)
    metrics: list[DemoDashboardMetric] = field(default_factory=list)
    quotations: list[DemoQuotation] = field(default_factory=list)
    invoices: list[DemoInvoice] = field(default_factory=list)
    activities: list[DemoActivity] = field(default_factory=list)
    enrollments: list[DemoEnrollment] = field(default_factory=list)
    total_leads: int = 0
    total_revenue: str = "$0"
    conversion_rate: str = "0%"
    active_students: int = 0


def generate_showcase_data() -> DemoShowcaseData:
    # ── Pipeline Stages ──────────────────────────────────────

    new_leads = [
        DemoLead(
            name="Sofia Martinez",
            country="Spain",
            program="General English",
            source="Landing Page",
            stage="New",
            assigned_to="Carlos R.",
            age=19,
            time_ago="2h ago",
            flag="🇪🇸",
        ),
        DemoLead(
            name="Luca Rossi",
            country="Italy",
            program="Business English",
            source="Facebook Ad",
            stage="New",
            assigned_to="Maria L.",
            age=24,
            time_ago="3h ago",
            flag="🇮🇹",
        ),
        DemoLead(
            name="Emma Johansson",
            country="Sweden",
            program="IELTS Preparation",
            source="Website Form",
            stage="New",
            assigned_to="Unassigned",
            age=22,
            time_ago="5h ago",
            flag="🇸🇪",
        ),
        DemoLead(
            name="Liam O'Brien",
            country="Ireland",
            program="Work & Study Dublin",
            source="Referral",
            stage="New",
            assigned_to="Carlos R.",
            age=23,
            time_ago="8h ago",
            flag="🇮🇪",
        ),
        DemoLead(
            name="Yuki Tanaka",
            country="Japan",
            program="English + Internship",
            source="Instagram",
            stage="New",
            assigned_to="Unassigned",
            age=21,
            time_ago="12h ago",
            flag="🇯🇵",
        ),
    ]

    contacted_leads = [
        DemoLead(
            name="Ana Gonzalez",
            country="Mexico",
            program="Cambridge Exam Prep",
            source="Landing Page",
            stage="Contacted",
            assigned_to="Maria L.",
            age=25,
            time_ago="Yesterday",
            flag="🇲🇽",
            days_in_stage=2,
        ),
        DemoLead(
            name="Pierre Dubois",
            country="France",
            program="French → English Immersion",
            source="Website Form",
            stage="Contacted",
            assigned_to="Carlos R.",
            age=20,
            time_ago="Yesterday",
            flag="🇫🇷",
            days_in_stage=1,
        ),
        DemoLead(
            name="Hannah Müller",
            country="Germany",
            program="Academic Year Abroad",
            source="Facebook Ad",
            stage="Contacted",
            assigned_to="Maria L.",
            age=18,
            time_ago="2 days ago",
            flag="🇩🇪",
            days_in_stage=3,
        ),
    ]

    qualified_leads = [
        DemoLead(
            name="Carlos Silva",
            country="Brazil",
            program="General English + Homestay",
            source="Quotation Request",
            stage="Qualified",
            assigned_to="Carlos R.",
            age=28,
            time_ago="3 days ago",
            flag="🇧🇷",
            days_in_stage=2,
        ),
        DemoLead(
            name="Miyazaki Kenji",
            country="Japan",
            program="Business English",
            source="Referral",
            stage="Qualified",
            assigned_to="Maria L.",
            age=31,
            time_ago="4 days ago",
            flag="🇯🇵",
            days_in_stage=1,
        ),
    ]

    proposal_leads = [
        DemoLead(
            name="Valentina Russo",
            country="Italy",
            program="Work & Study Sydney",
            source="Website Form",
            stage="Proposal Sent",
            assigned_to="Carlos R.",
            age=24,
            time_ago="1 week ago",
            flag="🇮🇹",
            days_in_stage=3,
            quotation_amount="€4,850",
            quotation_status="sent",
        ),
        DemoLead(
            name="Nora Kovács",
            country="Hungary",
            program="IELTS + University Pathway",
            source="Facebook Ad",
            stage="Proposal Sent",
            assigned_to="Maria L.",
            age=22,
            time_ago="5 days ago",
            flag="🇭🇺",
            days_in_stage=2,
            quotation_amount="€3,200",
            quotation_status="sent",
        ),
        DemoLead(
            name="Omar Hassan",
            country="Egypt",
            program="English for Engineering",
            source="Landing Page",
            stage="Proposal Sent",
            assigned_to="Carlos R.",
            age=26,
            time_ago="6 days ago",
            flag="🇪🇬",
            days_in_stage=4,
            quotation_amount="€2,750",
            quotation_status="draft",
        ),
    ]

    negotiation_leads = [
        DemoLead(
            name="Aisha Patel",
            country="India",
            program="MBA Preparation",
            source="Referral",
            stage="Negotiation",
            assigned_to="Maria L.",
            age=27,
            time_ago="1 week ago",
            flag="🇮🇳",
            days_in_stage=5,
            quotation_amount="€5,600",
            quotation_status="negotiating",
        ),
        DemoLead(
            name="Jorge Torres",
            country="Colombia",
            program="English + Internship",
            source="Quotation Request",
            stage="Negotiation",
            assigned_to="Carlos R.",
            age=23,
            time_ago="2 weeks ago",
            flag="🇨🇴",
            days_in_stage=7,
            quotation_amount="€3,950",
            quotation_status="negotiating",
        ),
    ]

    converted_leads = [
        DemoLead(
            name="Marco Bianchi",
            country="Italy",
            program="General English Sydney",
            source="Website Form",
            stage="Converted",
            assigned_to="Carlos R.",
            age=22,
            time_ago="3 weeks ago",
            flag="🇮🇹",
            quotation_amount="€2,800",
            quotation_status="approved",
        ),
        DemoLead(
            name="Sarah Chen",
            country="Taiwan",
            program="Academic Year Canada",
            source="Facebook Ad",
            stage="Converted",
            assigned_to="Maria L.",
            age=19,
            time_ago="2 weeks ago",
            flag="🇹🇼",
            quotation_amount="€8,200",
            quotation_status="approved",
        ),
    ]

    # ── Dashboard Metrics ────────────────────────────────────

    metrics = [
        DemoDashboardMetric(
            label="New Leads (This Month)",
            value="94",
            change="+18%",
            change_type="up",
            icon="M17 20V4M10 20l-7-7 7-7",
        ),
        DemoDashboardMetric(
            label="Revenue Enrolled",
            value="€47,200",
            change="+12%",
            change_type="up",
            icon="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6",
        ),
        DemoDashboardMetric(
            label="Conversion Rate",
            value="23.4%",
            change="+3.2%",
            change_type="up",
            icon="M22 12h-4l-3 9L9 3l-3 9H2",
        ),
        DemoDashboardMetric(
            label="Active Students",
            value="128",
            change="+8",
            change_type="up",
            icon="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 7a4 4 0 1 0 0-8 4 4 0 0 0 0 8z",
        ),
        DemoDashboardMetric(
            label="Outstanding Balance",
            value="€12,350",
            change="-5%",
            change_type="down",
            icon="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6",
        ),
        DemoDashboardMetric(
            label="Unassigned Leads",
            value="8",
            change="+2",
            change_type="up",
            icon="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6",
        ),
    ]

    # ── Quotations ───────────────────────────────────────────

    quotations = [
        DemoQuotation(
            "Q-2026-0034",
            "Valentina Russo",
            "Sydney",
            "Work & Study (24 wks)",
            "€4,850",
            "EUR",
            "sent",
            "Mar 12, 2026",
            24,
        ),
        DemoQuotation(
            "Q-2026-0033",
            "Nora Kovács",
            "London",
            "IELTS Prep (12 wks)",
            "€3,200",
            "EUR",
            "sent",
            "Mar 10, 2026",
            12,
        ),
        DemoQuotation(
            "Q-2026-0032",
            "Aisha Patel",
            "Toronto",
            "MBA Prep (36 wks)",
            "€5,600",
            "EUR",
            "negotiating",
            "Mar 8, 2026",
            36,
        ),
        DemoQuotation(
            "Q-2026-0031",
            "Jorge Torres",
            "Barcelona",
            "English + Internship (16 wks)",
            "€3,950",
            "EUR",
            "negotiating",
            "Mar 5, 2026",
            16,
        ),
        DemoQuotation(
            "Q-2026-0030",
            "Omar Hassan",
            "Manchester",
            "English for Engineering (8 wks)",
            "€2,750",
            "EUR",
            "draft",
            "Mar 3, 2026",
            8,
        ),
        DemoQuotation(
            "Q-2026-0029",
            "Marco Bianchi",
            "Sydney",
            "General English (12 wks)",
            "€2,800",
            "EUR",
            "approved",
            "Feb 28, 2026",
            12,
        ),
        DemoQuotation(
            "Q-2026-0028",
            "Sarah Chen",
            "Vancouver",
            "Academic Year (48 wks)",
            "€8,200",
            "EUR",
            "approved",
            "Feb 25, 2026",
            48,
        ),
        DemoQuotation(
            "Q-2026-0027",
            "Lena Schmidt",
            "Dublin",
            "Business English (8 wks)",
            "€1,950",
            "EUR",
            "approved",
            "Feb 22, 2026",
            8,
        ),
    ]

    # ── Invoices ─────────────────────────────────────────────

    invoices = [
        DemoInvoice(
            "INV-2026-0018",
            "Marco Bianchi",
            "€2,800",
            "paid",
            "Mar 15, 2026",
            "€2,800",
        ),
        DemoInvoice(
            "INV-2026-0017",
            "Sarah Chen",
            "€8,200",
            "paid",
            "Mar 20, 2026",
            "€8,200",
        ),
        DemoInvoice(
            "INV-2026-0016",
            "Lena Schmidt",
            "€1,950",
            "paid",
            "Mar 10, 2026",
            "€1,950",
        ),
        DemoInvoice(
            "INV-2026-0015",
            "Valentina Russo",
            "€4,850",
            "due",
            "Apr 5, 2026",
            "€0",
        ),
        DemoInvoice(
            "INV-2026-0014",
            "Nora Kovács",
            "€3,200",
            "due",
            "Apr 12, 2026",
            "€0",
        ),
        DemoInvoice(
            "INV-2026-0013",
            "Carlos Silva",
            "€2,400",
            "overdue",
            "Feb 28, 2026",
            "€1,200",
        ),
        DemoInvoice(
            "INV-2026-0012",
            "Miyazaki Kenji",
            "€3,600",
            "overdue",
            "Feb 20, 2026",
            "€0",
        ),
    ]

    # ── Enrollments ──────────────────────────────────────────

    enrollments = [
        DemoEnrollment(
            "Marco Bianchi",
            "General English - Sydney",
            "Jun 10, 2026",
            "enrolled",
            "€2,800",
        ),
        DemoEnrollment(
            "Sarah Chen",
            "Academic Year - Vancouver",
            "Sep 1, 2026",
            "enrolled",
            "€8,200",
        ),
        DemoEnrollment(
            "Lena Schmidt",
            "Business English - Dublin",
            "Apr 15, 2026",
            "enrolled",
            "€1,950",
        ),
        DemoEnrollment(
            "David Kim",
            "English + Internship - Toronto",
            "May 1, 2026",
            "pending",
            "€4,200",
        ),
        DemoEnrollment(
            "Elena Popescu",
            "IELTS Prep - London",
            "Pending start date",
            "pending",
            "€2,100",
        ),
    ]

    # ── Recent Activity ─────────────────────────────────────

    activities = [
        DemoActivity(
            "New Lead",
            "Sofia Martinez — General English, Dublin",
            "2 hours ago",
            "lead",
        ),
        DemoActivity(
            "New Lead",
            "Luca Rossi — Business English, London",
            "3 hours ago",
            "lead",
        ),
        DemoActivity(
            "Quotation Sent",
            "Valentina Russo — €4,850 · Work & Study Sydney",
            "4 hours ago",
            "quotation",
        ),
        DemoActivity(
            "WhatsApp Message",
            "Template 'Welcome' sent to Ana Gonzalez",
            "6 hours ago",
            "email",
        ),
        DemoActivity(
            "Invoice Paid",
            "Marco Bianchi — €2,800 · Invoice INV-2026-0018",
            "1 day ago",
            "invoice",
        ),
        DemoActivity(
            "Status Change",
            "Carlos Silva → Qualified (was Contacted)",
            "1 day ago",
            "lead",
        ),
        DemoActivity(
            "Quotation Approved",
            "Sarah Chen — €8,200 · Invoice created automatically",
            "2 days ago",
            "quotation",
        ),
        DemoActivity(
            "New Enrollment",
            "Lena Schmidt — Business English, Dublin · Start Apr 15",
            "2 days ago",
            "enrollment",
        ),
        DemoActivity(
            "Email Opened",
            "Nora Kovács opened quotation email",
            "3 days ago",
            "email",
        ),
        DemoActivity(
            "Payment Reminder",
            "Carlos Silva — €1,200 partial payment received",
            "3 days ago",
            "invoice",
        ),
        DemoActivity(
            "Facebook Lead",
            "Emma Johansson — IELTS Preparation, Cambridge",
            "5 hours ago",
            "lead",
        ),
        DemoActivity(
            "Lead Assigned",
            "Yuki Tanaka → Assigned to Maria L.",
            "8 hours ago",
            "lead",
        ),
    ]

    # ── Build pipeline dict ──────────────────────────────────

    pipeline = {
        "New": new_leads,
        "Contacted": contacted_leads,
        "Qualified": qualified_leads,
        "Proposal Sent": proposal_leads,
        "Negotiation": negotiation_leads,
        "Converted": converted_leads,
    }

    return DemoShowcaseData(
        pipeline_stages=pipeline,
        metrics=metrics,
        quotations=quotations,
        invoices=invoices,
        activities=activities,
        enrollments=enrollments,
        total_leads=94,
        total_revenue="€47,200",
        conversion_rate="23.4%",
        active_students=128,
    )
