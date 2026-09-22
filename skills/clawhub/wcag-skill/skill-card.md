## Description:

Build, audit, and repair web content against WCAG 2.2. Use when creating accessible HTML/CSS/JS, remediating accessibility defects, running reproducible automated audits, preparing WCAG 2.2 AAA evidence and human-test records, or running the optional AI-WCAG-Gauntlet benchmark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers, accessibility reviewers, and engineering teams use this skill to build accessible web pages, run local WCAG 2.2 audit workflows, triage findings, and prepare manual evidence for higher-conformance claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local audit workflow launches browser-based tools and fetches the URL under test.

Mitigation: Run it against local or trusted test URLs and provide explicit Chrome or Chromedriver paths when auto-detection is insufficient.

Risk: Automated accessibility tools can miss issues or return warnings, incomplete results, and false positives.

Mitigation: Review generated reports, preserve raw findings, and complete the manual protocol before relying on conformance claims.

Risk: Benchmark templates are reference material and copying them into benchmark submissions would invalidate benchmark results.

Mitigation: Use benchmark material only for explicit benchmark tasks and create original submissions tailored to the prompt.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/turbolego/skills/wcag-skill)
- [Project homepage](https://github.com/turbolego/wcag-skill)
- [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Reproducible validator workflow](references/validator-workflow.md)
- [WCAG 2.2 AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Mandatory human-test protocol](references/manual-test-protocol.md)
- [Optional AI-WCAG-Gauntlet extension](benchmark/README.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and report-oriented remediation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to produce or retain local accessibility reports such as axe, Pa11y, QualWeb, and W3C validator JSON outputs.]

## Skill Version(s):

2.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
