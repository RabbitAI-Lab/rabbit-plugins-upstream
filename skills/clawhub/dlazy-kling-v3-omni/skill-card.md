## Description:

Versatile video generation with Kling v3 Omni, supporting multi-modal image and prompt inputs for dynamic video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Kling v3 Omni video-generation service from an agent workflow, including text-to-video and image/video-conditioned generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided local media paths may be sent to dLazy's hosted service, and local media may be uploaded for model processing.

Mitigation: Use the skill only for content intended for dLazy processing, and avoid passing sensitive prompts or media unless that data handling is acceptable.

Risk: Authenticated generation requests may consume dLazy account credits.

Mitigation: Confirm account and cost expectations before execution; use the CLI's dry-run behavior where appropriate before making a generation call.

Risk: A global CLI install and saved API key can persist on the local system.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for per-invocation use when persistent installation or saved credentials are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or asynchronous task identifiers from the dLazy service.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
