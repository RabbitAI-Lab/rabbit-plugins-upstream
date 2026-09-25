## Description:

Build, audit, and repair web content against WCAG 2.2. Use when: (1) creating accessible HTML/CSS/JS, (2) remediating accessibility defects, (3) running reproducible automated audits, (4) preparing WCAG 2.2 AAA evidence and human-test records, or (5) running the optional AI-WCAG-Gauntlet benchmark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers, designers, and accessibility reviewers use this skill to build accessible web pages, run automated WCAG-oriented audits, triage findings, repair defects, and prepare WCAG 2.2 AAA evidence with required human-test records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated accessibility tools can be mistaken for proof of WCAG conformance.

Mitigation: Treat automated results as evidence, review incomplete and warning items, and complete the manual protocol and evidence matrix before making conformance claims.

Risk: Audit scripts fetch target pages and run third-party Node-based accessibility tools.

Mitigation: Run audits only against intended URLs, review the installed toolchain in the deployment environment, and keep reports scoped to the assessed site or application.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/turbolego/skills/wcag-skill)
- [Project homepage](https://github.com/turbolego/wcag-skill)
- [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Reproducible validator workflow](references/validator-workflow.md)
- [WCAG 2.2 AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Mandatory human-test protocol](references/manual-test-protocol.md)
- [Optional AI-WCAG-Gauntlet extension](benchmark/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples and optional JSON accessibility audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Automated audit output is evidence only; WCAG conformance claims require scoped manual review and documented evidence.]

## Skill Version(s):

2.0.12 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
