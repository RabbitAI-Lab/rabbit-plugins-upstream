## Description:

Routes Cargo workspace tasks to the right CLI skill and explains how to coordinate commands, identifiers, and workflows across Cargo domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Cargo workspace users use this router to select the relevant Cargo skill, plan multi-domain work, and follow CLI workflows for onboarding, data operations, and workspace management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refreshing the skill bundle or global CLI from mutable sources can change agent behavior unexpectedly.

Mitigation: Review the external installer before use and avoid automatic refreshes when reproducibility matters.

Risk: CLI operations can modify the wrong Cargo workspace if the active workspace is not checked.

Mitigation: Confirm the active workspace before running write commands.

Risk: Session shares and support reports can disclose sensitive session or record information to Cargo services.

Mitigation: Obtain consent before sharing and remove secrets and sensitive record data from reports.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills project homepage](https://github.com/getcargohq/cargo-skills)
- [CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline CLI commands and examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authenticated workspace for actionable operations.]

## Skill Version(s):

1.26.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
