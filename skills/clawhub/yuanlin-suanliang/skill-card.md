## Description:

Analyzes landscape CAD-derived candidates to estimate plant quantities and paving areas, producing confidence-tiered budget and material-plan drafts with evidence coordinates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Landscape quantity surveyors and design teams use the skill to prepare preliminary plant-count and paving-area estimates from landscape drawings. They review confidence tiers and evidence coordinates before relying on the resulting budget or material-plan drafts.

### Deployment Geography for Use:

Global; designed for Chinese-language landscape and construction drawings, with common English legend aliases.

## Known Risks and Mitigations:

Risk: Optional shared-state integration may execute an unverified local client and store project data outside the core quantity workflow.

Mitigation: Use the core quantity tools without shared-state integration until the client installation and data location are verified; SKILLBUS_DISABLE=1 blocks external-client execution while allowing local state storage.

Risk: Shared drafts may be marked confirmed without review, and fallback retrieval can make their contents or dates unreliable.

Mitigation: Independently inspect shared draft contents and dates, and confirm status before reusing any shared quantities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)

## Skill Output:

**Output Type(s):** [XLSX spreadsheets, CSV files, Markdown reports, Quantity-takeoff guidance]

**Output Format:** [XLSX, CSV, and Markdown budget and material-plan drafts, with evidence-coordinate notes for review candidates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence tiers P0–P3; draft estimates only, not design approval, settlement, completed-quantity measurement, or formal quotation.]

## Skill Version(s):

0.4.26 (source: server-resolved release and CHANGELOG.md, released 2026-10-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
