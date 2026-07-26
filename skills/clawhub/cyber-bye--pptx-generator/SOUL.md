---
name: pptx-generator-soul
description: Soul context for pptx-generator skill. Tracks presentation projects, active specs, generation history, and design preferences.
---

# PowerPoint Generator — Soul Context

## [WORKSPACE OWNER]
<!-- Loaded from core-extra/config/profile.md at runtime -->
- Owner:  [core-extra/config/profile.md → Owner.name]
- Skill:  pptx-generator
- Version: 1.0.0

---

## [ACTIVE PROJECTS]
<!-- Presentations currently being worked on. -->
<!-- Format: PROJECT | SPEC_FILE | OUTPUT_FILE | STATUS | SLIDES -->

---

## [COMPLETED DECKS]
<!-- Recently generated presentations. -->
<!-- Format: DATE | FILE | SLIDES | TYPE | STATUS -->

---

## [DESIGN PREFERENCES]
<!-- Default design choices. Set per session. -->
- default_font_title: Georgia
- default_font_body: Calibri
- default_primary: "1B1F3B"
- default_secondary: "708090"
- default_accent: "E4572E"

---

## [ERROR LOG]
<!-- Failed generation attempts. -->
<!-- Format: DATE | SPEC | ERROR | RESOLVED -->

---

## [SESSION LOG]
<!-- Append-only. -->
<!-- Format: YYYY-MM-DD | action:generate/read/edit | spec:name | output:file | slides:N -->
