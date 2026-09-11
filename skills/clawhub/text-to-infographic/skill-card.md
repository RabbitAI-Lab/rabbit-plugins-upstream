## Description:

Text to Infographic turns complex workflows, analysis notes, dashboards, and knowledge summaries into validated, editable single-page infographic plans and rendered HTML, PNG, SVG, whiteboard, or document outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and knowledge workers use this skill to compress complex information into scannable overview visuals while preserving editable source plans, evidence bindings, and downstream handoff options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted infographic plans can cause unexpected browser network requests during HTML or PNG rendering.

Mitigation: Render trusted plans by default; when accepting plans from others, restrict palette values to safe color formats and block non-file and non-data network requests during PNG capture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Infographic plan schema](schemas/infographic-plan.schema.json)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [JSON infographic plans, self-contained HTML, optional PNG images, SVG or whiteboard adapter drafts, and Markdown guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-aware plans render visible source, metric, claim, baseline, and annotation summaries and produce a colocated evidence JSON sidecar.]

## Skill Version(s):

0.5.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
