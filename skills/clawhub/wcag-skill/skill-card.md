## Description:

Build, audit, and repair web content against WCAG 2.2. Use when: (1) creating accessible HTML/CSS/JS, (2) remediating accessibility defects, (3) running reproducible automated audits, (4) preparing WCAG 2.2 AAA evidence and human-test records, or (5) running the optional AI-WCAG-Gauntlet benchmark. For benchmarks, require an unscored preflight of tag coverage, W3C, axe, Pa11y, and QualWeb before the first scored run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers and accessibility specialists use this skill to build and remediate web pages against WCAG 2.2, run repeatable automated audits, and prepare AAA evidence with manual testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and could not resolve several local references, so it does not establish that the skill is risk-free.

Mitigation: Review unresolved references and the skill contents before installation.

Risk: Audit scripts load the target URL, redirects, and browser subresources.

Mitigation: Audit only authorized URLs and prefer loopback or staging hosts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/turbolego/skills/wcag-skill)
- [Project homepage](https://github.com/turbolego/wcag-skill)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Validator workflow](references/validator-workflow.md)
- [AAA evidence matrix](references/aaa-evidence-matrix.md)
- [Manual test protocol](references/manual-test-protocol.md)
- [Dynamic-state test protocol](references/dynamic-state-test-protocol.md)
- [Legacy markup repair guide](references/legacy-markup-repair.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance, Analysis, Files]

**Output Format:** [Markdown, HTML/CSS/JavaScript code, shell commands, and JSON audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output varies by task; automated audit reports are evidence, not proof of WCAG conformance.]

## Skill Version(s):

2.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
