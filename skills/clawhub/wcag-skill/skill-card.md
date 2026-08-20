## Description:

Build, audit, and repair web content against WCAG 2.2, including accessible HTML/CSS/JS creation, accessibility remediation, reproducible automated audits, WCAG 2.2 AAA evidence records, human-test records, and optional benchmark support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and accessibility reviewers use this skill to build accessible web pages, triage and fix accessibility defects, run browser-based validation tooling, and prepare evidence for WCAG 2.2 AA or AAA review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated accessibility tools can miss issues or produce warnings that require judgment, so clean reports do not prove WCAG conformance.

Mitigation: Treat automated output as evidence only, review incomplete or warning results, and complete the manual protocol and evidence matrix before making AA or AAA conformance claims.

Risk: Browser-based audit tooling fetches target pages and writes reports locally, which may expose sensitive page content in generated artifacts.

Mitigation: Run audits only against intended targets, store reports in approved locations, and review generated files before sharing or publishing them.

Risk: The publishing helper can upload the skill to ClawHub when run with a valid CLAWHUB_TOKEN.

Mitigation: Do not run scripts/publish-web.py unless publishing is intended, and protect CLAWHUB_TOKEN as a deployment credential.

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

**Output Format:** [Markdown guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference local JSON accessibility reports from axe, Pa11y, QualWeb, and the Nu HTML checker when the audit scripts are run.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
