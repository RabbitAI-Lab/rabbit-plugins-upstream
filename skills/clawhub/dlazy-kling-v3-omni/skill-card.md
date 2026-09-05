## Description:

Versatile video generation with Kling v3 Omni, supporting prompt, image, and reference media inputs for dynamic video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and creators use this skill to generate short videos through the dLazy CLI using text prompts, images, and optional reference video inputs. It is suited for workflows that can send prompts and selected media to dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's hosted service.

Mitigation: Avoid uploading sensitive prompts or media unless the user accepts the cloud-processing workflow.

Risk: The CLI can persist an API key in the user's local configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for less persistent setup, and rotate or revoke stored keys when needed.

Risk: Generated outputs are hosted remotely and usage may consume account credits.

Mitigation: Confirm credit availability and sharing expectations before running generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; generated media URLs are hosted by dLazy.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
