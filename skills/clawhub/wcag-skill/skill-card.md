## Description:

Build, audit, and repair web content against WCAG 2.2, with reproducible automated checks and evidence-based manual testing for AAA work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[turbolego](https://clawhub.ai/user/turbolego)

### License/Terms of Use:

MIT

## Use Case:

Developers and accessibility practitioners use this skill to create accessible web content, audit and repair existing pages, and document automated and manual WCAG 2.2 checks. It supports baseline, AA, and AAA work while requiring human evidence for conformance claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence, but coverage is partial because some references could not be resolved; the skill also uses executable audit scripts.

Mitigation: Review unresolved references and the audit scripts before installation. Use the scripts with intended target URLs and the host's execution controls.

## Reference(s):

- [Validator workflow](artifact/references/validator-workflow.md)
- [AAA evidence matrix](artifact/references/aaa-evidence-matrix.md)
- [Manual test protocol](artifact/references/manual-test-protocol.md)
- [Dynamic state test protocol](artifact/references/dynamic-state-test-protocol.md)
- [Legacy markup repair](artifact/references/legacy-markup-repair.md)
- [Project homepage](https://github.com/turbolego/wcag-skill)
- [ClawHub release](https://clawhub.ai/turbolego/skills/wcag-skill)
- [Publisher profile](https://clawhub.ai/user/turbolego)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, Audit reports]

**Output Format:** [Markdown guidance with HTML/CSS/JavaScript examples, shell commands, and optional structured audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope and target conformance level are supplied by the user; automated results require human review and do not establish WCAG conformance.]

## Skill Version(s):

2.0.33 (source: SKILL.md frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
