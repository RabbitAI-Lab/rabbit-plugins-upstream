## Description:

Connects agents to dLazy's project-scoped sandbox assistant for multi-turn conversations and skill-driven tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to start or continue project-based conversations with dLazy's hosted sandbox agent, optionally attaching files for context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy's hosted service.

Mitigation: Only send data you intend to share with dLazy; review attachments before uploading.

Risk: The skill requires installing and authenticating a third-party CLI.

Mitigation: Review the pinned npm package or linked CLI source before installation, and rotate or revoke the dLazy API key when no longer needed.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming terminal text from the hosted agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports project-scoped, multi-turn conversations.]

## Skill Version(s):

1.2.30 (source: ClawHub release metadata; artifact frontmatter lists 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
