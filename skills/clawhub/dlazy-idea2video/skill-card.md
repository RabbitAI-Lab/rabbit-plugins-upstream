## Description:

Guides an agent from a creative idea through a confirmed video-production plan and canvas workflow, with dLazy CLI commands for media generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and external users can turn an idea into a reviewed story, scene, and shot plan, then prepare a canvas workflow for video generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands may run a locally installed CLI with a saved API key.

Mitigation: Review each proposed command before execution and use the CLI only when video generation was explicitly requested.

Risk: Prompts and referenced media files are sent to dLazy cloud endpoints.

Mitigation: Share only media and prompts approved for upload; review local API-key storage before signing in.

Risk: The artifact's CLI version references and embedded skill version differ from the release metadata.

Mitigation: Confirm the intended CLI version and review installation instructions before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source and usage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown plan summaries and generation commands; canvas workflow when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests confirmation before planning, canvas application, or individual generation commands.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
