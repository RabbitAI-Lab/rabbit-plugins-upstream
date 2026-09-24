## Description:

Coding workflow with planning, implementation, verification, and testing for clean software development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lion504](https://clawhub.ai/user/lion504)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill when they want an agent to follow a structured coding workflow for planning, implementation, progress tracking, verification, and delivery. The skill also provides guidance for saving coding preferences locally only when the user explicitly requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User preference notes can persist on local disk in ~/code/memory.md when explicitly saved.

Mitigation: Do not ask the skill to save credentials, secrets, sensitive personal data, or project-confidential details; edit or delete ~/code/memory.md when stored preferences are no longer needed.

## Reference(s):

- [Code 1.0.4 ClawHub Skill Page](https://clawhub.ai/lion504/skills/code-1-0-4)
- [lion504 Publisher Profile](https://clawhub.ai/user/lion504)
- [Code Skill Homepage](https://clawic.com/skills/code)
- [Skill Definition](artifact/SKILL.md)
- [Planning Reference](artifact/planning.md)
- [Execution Guidance](artifact/execution.md)
- [Verification Reference](artifact/verification.md)
- [Preference Storage Criteria](artifact/criteria.md)
- [Memory Template](artifact/memory-template.md)
- [State Tracking Guidance](artifact/state.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; may propose local preference files only when explicitly requested.]

## Skill Version(s):

1.0.4 (source: artifact/SKILL.md frontmatter); release 1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
