## Description:

Connects an agent to dLazy's project-scoped sandbox chat for multi-turn work with available skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or continue project-based conversations with a hosted sandbox agent, including tasks using available skills and optional file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional attached files are sent to dLazy's hosted services.

Mitigation: Avoid submitting sensitive prompts or files without authorization; review attachments before using --files.

Risk: CLI login stores an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent storage is undesirable.

Risk: Running the pinned third-party CLI requires trusting its package and publisher.

Mitigation: Confirm you trust dLazy and @dlazy/cli before installing or running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streaming conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses; results depend on the selected skill and prompt.]

## Skill Version(s):

1.2.32 (source: server-resolved release metadata; artifact frontmatter lists 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
