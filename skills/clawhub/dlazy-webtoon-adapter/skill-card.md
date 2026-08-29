## Description:

Adapts web-novel material into Chinese webtoon plot breakdowns, episode tags, and per-episode scripts, with dLazy CLI support for optional image-generation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and developers use this skill to turn supplied web-novel chapters into structured webtoon adaptation materials in Chinese. It can also guide controlled use of the dLazy CLI when image generation is part of the workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require dLazy account authentication and local API-key storage.

Mitigation: Use DLAZY_API_KEY for session-scoped credentials when possible, review the local CLI configuration location, and rotate or revoke keys from the dLazy dashboard when access is no longer needed.

Risk: Prompts and referenced media may be sent to dLazy API and file services during image-generation steps.

Mitigation: Do not submit sensitive, private, or rights-restricted source material unless the user has approved the cloud upload and applicable service terms.

Risk: The release evidence notes version mismatches and mixed workflow scope.

Mitigation: Review the installed CLI package and keep CLI commands under explicit user confirmation before executing generation steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Guidance]

**Output Format:** [Markdown prose with structured Chinese adaptation sections and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are conversation-facing adaptation documents and step-by-step command guidance; generated media URLs may be returned by the dLazy CLI.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
