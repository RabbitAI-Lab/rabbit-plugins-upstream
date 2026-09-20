## Description:

Build, audit, and repair web content against WCAG 2.2. Use when: (1) creating accessible HTML/CSS/JS, (2) remediating accessibility defects, (3) running reproducible automated audits, (4) preparing WCAG 2.2 AAA evidence and human-test records, or (5) running the optional AI-WCAG-Gauntlet benchmark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers and accessibility reviewers use this skill to build accessible web pages, run repeatable WCAG 2.2-oriented audits, triage findings, and prepare AAA evidence records when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes browser-based accessibility audit tools.

Mitigation: Install it only in environments where the listed tools are acceptable, and run checks only against pages you are authorized to test.

Risk: Auditing authenticated or private flows can expose sensitive page content in local reports.

Mitigation: Review the test scope before running audits and handle generated reports as local evidence with appropriate access controls.

Risk: Untrusted URLs or arbitrary Chrome launch arguments can increase execution risk.

Mitigation: Avoid passing untrusted URLs or Chrome extra arguments to the audit script.

Risk: Automated accessibility reports do not prove WCAG conformance.

Mitigation: Treat automated findings as evidence, then complete the documented manual review and AAA evidence matrix before making conformance claims.

## Reference(s):

- [Project homepage](https://github.com/turbolego/wcag-skill)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Reproducible validator workflow](references/validator-workflow.md)
- [WCAG 2.2 AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Mandatory human-test protocol](references/manual-test-protocol.md)
- [Optional AI-WCAG-Gauntlet extension](benchmark/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, code recommendations, and evidence templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON accessibility reports when the bundled audit scripts are run.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
