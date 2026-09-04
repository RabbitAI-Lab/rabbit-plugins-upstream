## Description:

Build, audit, and repair web content against WCAG 2.2, including accessible HTML/CSS/JS creation, defect remediation, reproducible automated audits, AAA evidence records, and optional AI-WCAG-Gauntlet benchmark checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and accessibility reviewers use this skill to build accessible pages, triage and fix WCAG 2.2 issues, run reproducible automated audits, and prepare human-test evidence for AA or AAA claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated accessibility tools can miss dynamic DOM states, authenticated flows, third-party components, and issues that require human judgment.

Mitigation: Run audits only against intended routes and states, review every warning or incomplete result, and complete the manual protocol and evidence matrix before making AA or AAA conformance claims.

Risk: The audit workflow installs and runs npm-based accessibility tooling plus browser dependencies.

Mitigation: Install the skill only in environments where those dependencies are acceptable, use the documented Chrome and Chromedriver paths when needed, and review generated reports before acting on them.

Risk: The optional AI-WCAG-Gauntlet benchmark materials can invalidate a benchmark if copied as a submission.

Mitigation: Use the benchmark extension only for explicit benchmark requests and create original submission files instead of copying templates.

## Reference(s):

- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Project homepage](https://github.com/turbolego/wcag-skill)
- [Reproducible validator workflow](references/validator-workflow.md)
- [WCAG 2.2 AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Mandatory human-test protocol](references/manual-test-protocol.md)
- [Optional AI-WCAG-Gauntlet extension](benchmark/README.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, code suggestions, and references to JSON audit reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Automated reports are evidence for review; they do not independently establish WCAG conformance.]

## Skill Version(s):

2.0.3 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
