## Description:

Routes Cargo tasks to the appropriate CLI skill and explains setup, workspace workflows, identifiers, asynchronous runs, and common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market teams use this router to choose the right Cargo skill for onboarding, workspace configuration, and cross-domain CLI tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup or refresh may install a global CLI and update the local skill bundle.

Mitigation: Review the first setup or refresh commands and prefer pinned versions before installation.

Risk: Cargo commands can change the active workspace and trigger paid or recurring actions.

Mitigation: Confirm the active workspace, intended changes, and costs before writes or recurring actions.

Risk: Sharing reports or session activity may disclose sensitive information.

Mitigation: Obtain approval and remove secrets and record-level data before sharing.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo use cases](artifact/references/use-cases.md)
- [Cargo prerequisites](artifact/references/prerequisites.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to domain-specific Cargo skills; does not itself execute commands.]

## Skill Version(s):

1.28.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
