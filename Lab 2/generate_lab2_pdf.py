"""
Generates PES1UG24CS387_SE_LAB2_Jira_Backlog_Sprint_Simulation.pdf
Using ReportLab
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
import os

def create_lab2_pdf():
    pdf_path = "PES1UG24CS387_SE_LAB2_Jira_Backlog_Sprint_Simulation.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1A365D'),
        alignment=1, # Center
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#4A5568'),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#2B6CB0'),
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SubSectionHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#2D3748'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )

    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#2D3748')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.white
    )

    story = []

    # Title & Header
    story.append(Paragraph("PES UNIVERSITY", title_style))
    story.append(Paragraph("Department of Computer Science & Engineering<br/><b>UE24CS351A — Software Engineering Laboratory</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2B6CB0'), spaceAfter=10))

    meta_data = [
        [Paragraph("<b>Student Name:</b> Roshan", body_style), Paragraph("<b>SRN:</b> PES1UG24CS387", body_style)],
        [Paragraph("<b>Lab 2 Title:</b> Agile Backlog Creation & Sprint Simulation in Jira", body_style), Paragraph("<b>Domain:</b> Plate Pilot (#19)", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[270, 260])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#EDF2F7')),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Epics
    story.append(Paragraph("1. Jira Epics Breakdown", h1_style))
    story.append(Paragraph("Functional and non-functional requirements from Lab 1 were decomposed into four major Agile Epics in Jira Software:", body_style))

    epics_data = [
        [Paragraph("Epic ID", table_header), Paragraph("Epic Title", table_header), Paragraph("Description", table_header), Paragraph("Mapped Reqs", table_header)],
        [Paragraph("<b>PP-EPIC-1</b>", table_cell), Paragraph("Personalized Dietary & Meal Planning Engine", table_cell), Paragraph("Algorithmic engine generating 7-day medical meal schedules adhering to calorie and allergen rules.", table_cell), Paragraph("FR-001, FR-005", table_cell)],
        [Paragraph("<b>PP-EPIC-2</b>", table_cell), Paragraph("Nutritional Adherence & Dynamic Adaptation", table_cell), Paragraph("Recalculating nutrition targets dynamically based on weekly weight logs and adherence trends.", table_cell), Paragraph("FR-002, FR-004", table_cell)],
        [Paragraph("<b>PP-EPIC-3</b>", table_cell), Paragraph("Order Scheduling, Logistics & Kitchen Dispatch", table_cell), Paragraph("Delivery pause/skip controls and 12-hour kitchen dispatch lockout enforcement.", table_cell), Paragraph("FR-003, NFR-001", table_cell)],
        [Paragraph("<b>PP-EPIC-4</b>", table_cell), Paragraph("Health Data Privacy, Security & Compliance", table_cell), Paragraph("AES-256 encryption at rest and strict clinical RBAC provider-subscriber isolation.", table_cell), Paragraph("NFR-002", table_cell)]
    ]
    epics_table = Table(epics_data, colWidths=[65, 140, 245, 80])
    epics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')]),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(epics_table)
    story.append(Spacer(1, 10))

    # 2. Product Backlog
    story.append(Paragraph("2. Product Backlog & Fibonacci Story Points", h1_style))
    story.append(Paragraph("Stories were formulated in <i>As a... I want... So that...</i> format and estimated using Planning Poker with Fibonacci numbers (1, 2, 3, 5, 8):", body_style))

    stories_data = [
        [Paragraph("ID", table_header), Paragraph("Epic", table_header), Paragraph("User Story (Role, Goal, Benefit)", table_header), Paragraph("SP", table_header), Paragraph("Pri", table_header)],
        [Paragraph("<b>PP-101</b>", table_cell), Paragraph("EPIC-1", table_cell), Paragraph("<b>As a</b> allergic subscriber, <b>I want</b> strict allergen filtering, <b>so that</b> meals avoid life-threatening reactions.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-102</b>", table_cell), Paragraph("EPIC-1", table_cell), Paragraph("<b>As a</b> subscriber, <b>I want</b> calorie and macro targets computed, <b>so that</b> meals align with metabolic goals.", table_cell), Paragraph("3", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-103</b>", table_cell), Paragraph("EPIC-1", table_cell), Paragraph("<b>As a</b> subscriber, <b>I want</b> 7-day meal schedules auto-compiled, <b>so that</b> I don't plan meals manually.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-201</b>", table_cell), Paragraph("EPIC-2", table_cell), Paragraph("<b>As a</b> subscriber, <b>I want</b> to log weekly weight and adherence, <b>so that</b> the team tracks progress.", table_cell), Paragraph("3", table_cell), Paragraph("Med", table_cell)],
        [Paragraph("<b>PP-202</b>", table_cell), Paragraph("EPIC-2", table_cell), Paragraph("<b>As a</b> system, <b>I want</b> to recalibrate macros dynamically, <b>so that</b> weight loss goals don't plateau.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-203</b>", table_cell), Paragraph("EPIC-2", table_cell), Paragraph("<b>As a</b> kitchen staff, <b>I want</b> allergen-safe ingredient substitution, <b>so that</b> stockouts don't halt prep.", table_cell), Paragraph("3", table_cell), Paragraph("Low", table_cell)],
        [Paragraph("<b>PP-301</b>", table_cell), Paragraph("EPIC-3", table_cell), Paragraph("<b>As a</b> subscriber, <b>I want</b> delivery pause/skip controls (<5s), <b>so that</b> I am not billed when away.", table_cell), Paragraph("3", table_cell), Paragraph("Med", table_cell)],
        [Paragraph("<b>PP-302</b>", table_cell), Paragraph("EPIC-3", table_cell), Paragraph("<b>As a</b> kitchen manager, <b>I want</b> a 12-hour dispatch lockout, <b>so that</b> fresh food prep is not disrupted.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-401</b>", table_cell), Paragraph("EPIC-4", table_cell), Paragraph("<b>As a</b> compliance officer, <b>I want</b> patient metabolic profiles encrypted at rest (AES-256), <b>so that</b> HIPAA is satisfied.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
        [Paragraph("<b>PP-402</b>", table_cell), Paragraph("EPIC-4", table_cell), Paragraph("<b>As a</b> dietitian, <b>I want</b> RBAC clinical barriers, <b>so that</b> only assigned patients are accessible.", table_cell), Paragraph("5", table_cell), Paragraph("High", table_cell)],
    ]
    stories_table = Table(stories_data, colWidths=[45, 50, 365, 30, 40])
    stories_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')]),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (3, 1), (4, -1), 'CENTER'),
    ]))
    story.append(stories_table)

    story.append(PageBreak())

    # 3. Sprints and Burndown
    story.append(Paragraph("3. Sprint Simulation & Burndown Analysis", h1_style))
    story.append(Paragraph("Two 10-day sprints were simulated in Jira. Work transitioned smoothly from To Do to In Progress to Done:", body_style))

    if os.path.exists("burndown_chart_sprint1.png"):
        story.append(Paragraph("<b>Sprint 1 Burndown Chart (Core Foundation & Security — 18 SP)</b>", h2_style))
        story.append(Image("burndown_chart_sprint1.png", width=520, height=240))
        story.append(Spacer(1, 10))

    if os.path.exists("burndown_chart_sprint2.png"):
        story.append(Paragraph("<b>Sprint 2 Burndown Chart (Adaptation, Logistics & RBAC — 16 SP)</b>", h2_style))
        story.append(Image("burndown_chart_sprint2.png", width=520, height=240))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # 4. Reflection Questions
    story.append(Paragraph("4. Reflection Questions", h1_style))

    q1 = "1. Did your estimations reflect the actual effort?"
    a1 = ("<b>Yes.</b> Fibonacci story point estimations accurately captured the technical complexity. "
          "5-point stories (PP-101 Allergen Filtering, PP-401 AES-256 Encryption, PP-202 Adaptive Recalibration) "
          "required multi-variable constraint solving, cryptographic key segregation, and boundary validation, "
          "taking 4 to 5 days each. Simpler 3-point stories (PP-102 Target Calculator, PP-201 Log Entry) involved "
          "straightforward arithmetic formulas and CRUD operations, finishing on Day 2 in both sprints. "
          "Decomposing stories into concrete acceptance criteria prevented estimation drift.")
    story.append(Paragraph(q1, h2_style))
    story.append(Paragraph(a1, body_style))
    story.append(Spacer(1, 6))

    q2 = "2. Was your backlog well-prioritized?"
    a2 = ("<b>Yes.</b> The backlog was prioritized using a hybrid of MoSCoW and Risk-Driven Prioritization. "
          "In Sprint 1, patient safety (Allergen Filtering, PP-101) and regulatory compliance (Data Encryption, PP-401) "
          "were scheduled first because delivering a meal generator without allergen guarantees creates immediate clinical risk, "
          "and retrofitting encryption after schema finalization is expensive. In Sprint 2, delivery logistics (PP-301, PP-302) "
          "and dynamic adaptation (PP-202) built on the proven Sprint 1 foundation. Optional capabilities like ingredient "
          "substitution (PP-203, Low priority) were safely deferred.")
    story.append(Paragraph(q2, h2_style))
    story.append(Paragraph(a2, body_style))
    story.append(Spacer(1, 6))

    q3 = "3. How did your simulated sprint align with your plan?"
    a3 = ("<b>The simulated sprints aligned exceptionally well with our sprint plans.</b> In Sprint 1, all 18 planned story "
          "points were completed with zero spillover; minor technical friction during cryptographic salt generation was absorbed "
          "between Days 5 and 7, allowing PP-103 to complete cleanly on Day 10. In Sprint 2, the team committed to 16 story points "
          "and completed all stories by Day 9 (one day ahead of schedule), creating a 1-day buffer for integration and automated "
          "test validation.")
    story.append(Paragraph(q3, h2_style))
    story.append(Paragraph(a3, body_style))
    story.append(Spacer(1, 6))

    q4 = "4. What insights did the burndown chart give about your team's capacity?"
    a4 = ("<b>The burndown charts revealed three key capacity insights:</b><br/>"
          "1. <b>Sustainable Team Velocity:</b> The team demonstrates a dependable velocity of <b>16 to 18 story points per 10-day sprint</b> "
          "(~1.6–1.8 SP/day). Overcommitting beyond 20 points would introduce severe delivery risk.<br/>"
          "2. <b>Healthy Step-Down Trajectory:</b> The actual remaining effort line decremented steadily across Days 2, 4, 7, and 10, "
          "tracking close to the grey guideline line. This proves work was broken down into independently deployable slices rather "
          "than creating an unhealthy 'cliff-drop' on the final day.<br/>"
          "3. <b>Buffer Management:</b> Completing Sprint 2 on Day 9 demonstrated that reserving a 10% capacity margin is essential "
          "to absorb code reviews, PR approvals, and CI/CD test runs without missing sprint commitments.")
    story.append(Paragraph(q4, h2_style))
    story.append(Paragraph(a4, body_style))

    doc.build(story)
    print(f"Generated PDF: {pdf_path}")

if __name__ == "__main__":
    create_lab2_pdf()
