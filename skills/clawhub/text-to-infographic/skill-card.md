## Description:

Text to Infographic compresses complex information into structured infographic plans and can render self-contained HTML, PNG share images, or SVG, whiteboard, and document adapter drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and knowledge workers use this skill to turn workflows, frameworks, analysis notes, dashboards, or planning material into a scannable one-page overview visual with an editable structured plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infographic plan JSON is processed locally and can cause HTML, PNG, or draft files to be written to local directories.

Mitigation: Use plans from trusted sources and choose output paths deliberately before rendering or exporting.

Risk: PNG export starts a local headless Chrome or Chromium instance.

Mitigation: Run PNG export only in an environment where local Chrome execution is acceptable, and keep HTML rendering as the default when a static image is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [README](artifact/README.md)
- [Infographic plan schema](artifact/schemas/infographic-plan.schema.json)
- [v0.3.0 premium visual upgrade notes](artifact/docs/v0.3.0-premium-visual-upgrade.md)
- [CHANGELOG](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with JSON infographic plans, self-contained HTML files, PNG exports, and adapter draft JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary output is a validated plan plus self-contained HTML; optional PNG export requires local Chrome or Chromium.]

## Skill Version(s):

0.3.0 (source: server release metadata and CHANGELOG, released 2026-09-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
