## Description:

Generate cinematic video assets with Google Veo 3.1 through the dLazy hosted service, supporting text-to-video, image-guided generation, and video extension workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or extend videos through the dLazy CLI and hosted Veo 3.1 workflow. It is suited for prompt-driven cinematic effects generation where cloud processing, uploaded media inputs, and hosted output URLs are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and selected media files are sent to dLazy hosted endpoints for processing.

Mitigation: Install only when hosted dLazy processing is intended, avoid submitting sensitive media unless approved, and confirm local file paths before upload.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY path or npx install path when a persistent saved key or global binary is not desired.

Risk: Video generation consumes dLazy API credits and generated files are hosted by dLazy.

Mitigation: Use dry-run or cost-estimate flows where available, monitor organization credits, and treat returned hosted URLs according to the user's data-sharing expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, local saved assets when requested, or asynchronous task identifiers for polling.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
