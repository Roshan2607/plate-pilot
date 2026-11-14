# Software Engineering Laboratory Submissions (Labs 1 – 7)

**Student Name:** Roshan  
**Student SRN:** PES1UG24CS387  
**Course Code:** UE24CS351A — Software Engineering  
**Department:** Computer Science & Engineering  
**GitHub Repository:** [Roshan2607/SE_LABS](https://github.com/Roshan2607/SE_LABS)

---

## 📋 Repository Overview

This repository consolidates all individual Software Engineering (SE) laboratory submissions (Labs 1 through 7) strictly aligned with the official PES University course handouts, problem statements, and evaluation criteria.

Each laboratory resides in its self-contained directory complete with:
- **Official Student Handout** (PDF / DOCX reference)
- **Submitted Student Deliverables** (Reports, PDFs, Diagrams, Worksheets)
- **Executable Source Code & Test Suites** (100% automated pass rate via `pytest`)
- **Technical Documentation & Reflection Analysis**

---

## 🗂️ Laboratory Directory Structure

```text
SE-Labs/
├── Lab 1/                   # Requirements Engineering & UML Use-Case Modelling (Plate Pilot)
│   ├── Lab1_student_handout.pdf      # Official PESU Lab 1 Handout
│   ├── Level 1_Labs_PES1UG24CS387.pdf# Submitted Requirements Table & Use-Case Document
│   ├── plate_pilot.py                # Executable domain model for FR-001 through FR-005
│   ├── test_plate_pilot.py           # Automated test suite (5 passed)
│   ├── use_case_diagram.png          # UML Use Case Diagram (Actors, Includes, Extends)
│   ├── use_case_diagram.pdf          # Vector PDF diagram
│   ├── use_case_diagram.mermaid      # Diagram source definition
│   └── README.md
├── Lab 2/                   # Agile Backlog Creation & Sprint Simulation in Jira (Plate Pilot)
│   ├── Lab_2_Jira_Student_Handout.pdf # Official PESU Lab 2 Handout
│   ├── PES1UG24CS387_SE_LAB2_Jira_Backlog_Sprint_Simulation.pdf # Deliverable PDF Report
│   ├── agile_simulation.py           # Scrum Project, Epics, Stories, Sprints & Burndown tracker
│   ├── generate_burndown_charts.py   # Publication-quality burndown chart visualizer
│   ├── generate_lab2_pdf.py          # ReportLab PDF compilation script
│   ├── test_agile_simulation.py      # Automated test suite (6 passed)
│   ├── burndown_chart_sprint1.png    # Sprint 1 Burndown Chart (18 SP)
│   ├── burndown_chart_sprint2.png    # Sprint 2 Burndown Chart (16 SP)
│   └── README.md                     # Epics, Stories, Boards & 4 Reflection Questions
├── Lab 3/                   # Architecture & Component Modelling (Plate Pilot)
│   ├── Lab_3_Architecture_Student_handout.pdf # Official PESU Lab 3 Handout
│   ├── Lab_3_Reference_Sheet(1).docx          # Official Reference Guide
│   ├── PES1UG24CS387_LAB3.pdf                 # 1-Page Written Architectural Justification
│   ├── component_diagram.png                  # UML Component Diagram (5 components, 4 interfaces)
│   ├── architecture_components.py             # 3-Tier Layered Architecture implementation
│   ├── test_architecture.py                  # Validates NFR-001 (<5s latency) & NFR-002 (security)
│   └── README.md
├── Lab 4/                   # AI-Assisted VibeCoding (Scenario 18: Blackjack vs Dealer)
│   ├── Lab_4_VibeCoding_Student_handout.pdf   # Official PESU Lab 4 Handout
│   ├── PES1UG24CS387 Lab 4 – Vibe Coding Deliverable Submission.pdf # Video Drive Links
│   ├── SE_LAB4_Prompts.pdf                    # Complete 31-page AI Prompt Transcript
│   ├── cards.py                               # Corrected Ace hand evaluation (soft/hard totals)
│   ├── game.py                                # Round mechanics, wagers, and multi-round bankroll
│   ├── main.py                                # Interactive game loop
│   ├── requirements.txt
│   ├── test_blackjack.py                      # Automated test suite (9 passed)
│   └── README.md
├── Lab 5/                   # Static Code Analysis (Bike Share Stations)
│   ├── Lab_5_Static_Code_Analysis_Student_handout.pdf # Official PESU Lab 5 Handout
│   ├── bike_share_stations.py                 # Refactored code (Pylint 10/10, Bandit 0 issues)
│   ├── issues.md                              # Static analysis defect ledger
│   ├── reflection.md                          # Technical reflection report
│   ├── reports/
│   │   ├── before/                            # Baseline reports (Bandit, Flake8, Pylint)
│   │   └── after/                             # Remediated clean reports (0 defects)
│   ├── test_bike_share_stations.py            # Functional test suite (5 passed)
│   └── README.md
├── Lab 6/                   # Code & Branch Coverage Analysis (Shopping Cart)
│   ├── Lab_6_Code&BranchCoverage_Student_Handout.docx (1).pdf # Official PESU Lab 6 Handout
│   ├── PES1UG24CS387_SE_LAB6.pdf              # Submitted coverage report with screenshots
│   ├── PES1UG24CS387_SE_LAB6.docx             # Submission report source
│   ├── shopping_cart.py                       # Application under test
│   ├── CodeCoverageTest_23_shopping_cart.py   # Statement Coverage suite (100%)
│   ├── BranchCoverageTest_23_shopping_cart.py # Branch Coverage suite (100% - 22/22 branches)
│   ├── test_shopping_cart.py                  # Unified test runner
│   └── README.md
├── Lab 7/                   # Fuzz Testing for Input Validation Bugs (Shopping Cart)
│   ├── Lab_7_FuzzTesting_Student_Handout.pdf  # Official PESU Lab 7 Handout
│   ├── PES1UG24CS387_LAB7_SE.pdf              # Submitted Fuzz Testing report with screenshots
│   ├── shopping_cart.py                       # Hardened against arbitrary fuzz inputs & None
│   ├── processor.py                           # Course handout alias
│   ├── test_shopping_cart.py                  # Hypothesis property-based fuzz tests
│   ├── test_processor.py                      # Handout test runner alias (6 passed)
│   └── README.md
├── .gitignore
├── README.md                # Master documentation
└── run_all_tests.py         # Automated runner across all 7 labs
```

---

## 📊 Summary of Labs & Verification Status

| Lab | Curriculum Title | Assigned Scenario | Deliverables & Artifacts | Automated Test Status |
| :---: | :--- | :--- | :--- | :---: |
| **Lab 1** | Requirements Engineering & UML Use-Case Modelling | Plate Pilot (#19) | 5 FRs, 2 NFRs, Use-Case Diagram, Flow Document, `plate_pilot.py` | **5 / 5 PASSED** |
| **Lab 2** | Agile Backlog Creation & Sprint Simulation in Jira | Plate Pilot (#19) | 4 Epics, 10 Stories (Fibonacci SP), 2 Sprints, Burndown Charts, 4 Reflection Answers | **6 / 6 PASSED** |
| **Lab 3** | Component Modelling & Architecture Selection | Plate Pilot (#19) | 1-Page Justification, 5 Components, 4 Interfaces, `test_architecture.py` | **3 / 3 PASSED** |
| **Lab 4** | AI-Assisted VibeCoding | Scenario 18: Blackjack | Tasks 1–4, Video Links, 31-page Prompts PDF, `test_blackjack.py` | **9 / 9 PASSED** |
| **Lab 5** | Static Code Analysis | Bike Share Stations | Pylint (10/10), Bandit (0 issues), Flake8 clean, Before/After reports | **5 / 5 PASSED** |
| **Lab 6** | Code & Branch Coverage Analysis | Shopping Cart | 100% Statement Coverage, 100% Branch Coverage (22/22 branches), Report PDF | **10 / 10 PASSED** |
| **Lab 7** | Fuzz Testing for Input Validation Bugs | Shopping Cart / Hypothesis | Hardened parser against arbitrary strings & nulls, 6 Hypothesis tests, Report PDF | **6 / 6 PASSED** |
| **TOTAL** | **All 7 Laboratories Consolidated** | **UE24CS351A** | **Unified Executable Repository** | **44 / 44 PASSED (100%)** |

---

## 🚀 Quick Start & Execution

### 1. Run Master Test Suite Across All Labs
Run the single root runner script to execute all automated test suites sequentially:

```bash
python run_all_tests.py
```

### 2. Run Individual Labs

#### **Lab 1: Requirements Engineering & UML Use-Case Modelling**
```bash
cd "Lab 1"
pytest test_plate_pilot.py -v
```

#### **Lab 2: Agile Backlog Creation & Sprint Simulation in Jira**
```bash
cd "Lab 2"
pytest test_agile_simulation.py -v
# Re-generate burndown charts & deliverable PDF:
python generate_burndown_charts.py
python generate_lab2_pdf.py
```

#### **Lab 3: Architecture & Component Modelling**
```bash
cd "Lab 3"
pytest test_architecture.py -v
```

#### **Lab 4: Scenario 18 — Blackjack**
```bash
cd "Lab 4"
pytest test_blackjack.py -v
# Or play the interactive game:
python main.py
```

#### **Lab 5: Static Code Analysis — Bike Share Stations**
```bash
cd "Lab 5"
pytest test_bike_share_stations.py -v
pylint bike_share_stations.py
bandit -r bike_share_stations.py
```

#### **Lab 6: Code & Branch Coverage Analysis**
```bash
cd "Lab 6"
pytest test_shopping_cart.py --cov=shopping_cart --cov-branch --cov-report=term-missing
```

#### **Lab 7: Fuzz Testing (Hypothesis)**
```bash
cd "Lab 7"
pytest test_processor.py -v
```
