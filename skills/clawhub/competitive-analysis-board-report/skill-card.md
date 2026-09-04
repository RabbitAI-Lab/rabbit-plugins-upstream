## Description:

This skill helps executives, general manager offices, and strategy teams produce aligned board-level competitive analysis deliverables from public competitive intelligence and optional company materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daikangjun19831230-kevin](https://clawhub.ai/user/daikangjun19831230-kevin)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, executives, GM offices, and strategy teams use this skill to convert competitive research into a board-ready DOCX decision-spine report and a 14-slide PPT. It is aimed at Chinese consumer, agricultural, and food-manufacturing companies that need evidence-graded competitor benchmarking and strategic decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitive intelligence and optional internal company PDFs may contain sensitive business information.

Mitigation: Treat provided company materials as confidential inputs and review generated deliverables before sharing or using them for business decisions.

Risk: Board recommendations can be misleading if public competitor data is stale, incomplete, or inconsistent.

Mitigation: Cross-check high-impact claims against official or company-provided sources and preserve the skill's A/B/C evidence grading in final reports.

Risk: Generated DOCX and PPTX deliverables may carry incorrect facts or formatting issues if scripts are adapted without validation.

Mitigation: Run the included PPT validator, extract and inspect DOCX text where relevant, and manually review strategic wording and layout before business use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/daikangjun19831230-kevin/skills/competitive-analysis-board-report)
- [Decision-Spine Competitive Analysis Methodology](artifact/references/methodology.md)
- [PPT Flow Layout Engine Notes](artifact/references/engine_notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python script usage that produces DOCX and PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces two aligned board deliverables when executed with the required Python document-generation dependencies and reviewed source data.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
