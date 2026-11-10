## Description:

Entry point for Cargo (getcargo.ai), go-to-market infrastructure for AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use Cargo as the entry point for go-to-market work: it routes requests to the right Cargo skill and provides shared guidance for setup, runs, batches, asynchronous polling, and common failure cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install or refresh steps may use unpinned versions.

Mitigation: Review and pin the package and skill versions before installing or refreshing.

Risk: Support reports may disclose commands or workspace details.

Mitigation: Review report contents and remove command or workspace details that are not needed before submitting.

Risk: The security inspection was partial, and some actions extend beyond the skill's routing purpose.

Mitigation: Inspect the requested commands and their scope before execution; treat the scan as incomplete assurance.

## Reference(s):

- [Cargo Skills project homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo CLI package](https://www.npmjs.com/package/@cargo-ai/cli)
- [Prerequisites](artifact/references/prerequisites.md)
- [Common gotchas](artifact/references/gotchas.md)
- [End-to-end use cases](artifact/references/use-cases.md)
- [Interaction conventions](artifact/references/interaction.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific routing and operational guidance.]

## Skill Version(s):

1.36.2 (source: frontmatter; server release 1.36.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
