## Description:

Router and overview for the Cargo CLI agent skills, covering skill routing, declarative CDK versus imperative CLI use, UUID flow, async polling, end-to-end Cargo use cases, and common gotchas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this router skill to choose the right Cargo CLI capability skill, understand workspace setup and authentication, and coordinate Cargo workflows such as enrichment, CRM sync, diagnostics, hosted apps, workspace-as-code, and GTM context authoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer hooks may persist across sessions and auto-approve Cargo actions.

Mitigation: Prefer the documented npm or plugin install path, review installed hooks, and install only when the Cargo publisher is trusted.

Risk: Workspace writes, deploys, deletes, token creation, user invites, and paid batches can change data, permissions, costs, or production behavior.

Mitigation: Confirm the active workspace, keep API tokens scoped and out of chat or logs, and require explicit review before privileged, destructive, deploy, or paid batch actions.

Risk: The evidence records no server-resolved GitHub import provenance for this version.

Mitigation: Use the server-resolved publisher profile and ClawHub skill page for ownership context, and do not infer repository provenance from skill text alone.

## Reference(s):

- [Cargo skill page](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples and cross-reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent toward Cargo CLI commands and related Cargo skill references; Cargo CLI command results are JSON when executed.]

## Skill Version(s):

1.16.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
