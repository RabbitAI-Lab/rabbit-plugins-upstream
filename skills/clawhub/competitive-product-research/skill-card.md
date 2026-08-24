## Description:

Dual-track competitive research: experience benchmarking across eight UX dimensions plus strategic diagnostics using SWOT, Five Forces, and PESTLE, producing source-traceable HTML or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chris1wang3](https://clawhub.ai/user/chris1wang3)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, UX researchers, strategy teams, and founders use this skill to benchmark competitors, diagnose experience and market-positioning gaps, and produce an evidence-linked report for planning or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The intake flow may pass research parameters through the host agent flow or clipboard, which can expose private PRDs, screenshots, or internal metrics if users paste sensitive material.

Mitigation: Treat user-supplied competitive materials as sensitive, redact before external sharing, and verify that generated reports do not include confidential details unless explicitly intended.

Risk: The bundled Chrome regression test is intended for form-development validation and launches a local browser session.

Mitigation: Run the regression test only when modifying the intake form asset and review the local environment before executing it.

## Reference(s):

- [Research Playbook](artifact/references/research-playbook.md)
- [Professional HTML Report Template](artifact/references/report-template-pro.html)
- [Intake Form](artifact/assets/intake-form.html)
- [ClawHub Skill Page](https://clawhub.ai/chris1wang3/skills/competitive-product-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [HTML or Markdown competitive research report with evidence labels, source index, key findings, benchmark tables, and roadmap recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SRC-xxx evidence labels and requires public-source links in HTML reports to open directly when URLs are available.]

## Skill Version(s):

1.4.8 (source: SKILL.md frontmatter, claw.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
