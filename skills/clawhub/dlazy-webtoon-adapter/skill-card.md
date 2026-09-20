## Description:

Helps adapt web novels into Chinese webtoon drama outputs, including genre setup, plot breakdown, episode tagging, per-episode scripts, and optional dLazy CLI image-generation workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers can use this skill to turn web-novel material into structured Chinese webtoon adaptation drafts, including plot breakdowns, episode tags, and episode scripts. When image generation is requested, it also guides reviewed, step-by-step use of the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to install or run the dLazy CLI and authenticate with dLazy services.

Mitigation: Review the skill before installation and run CLI commands only when the user explicitly requests generation.

Risk: Prompts and selected local media may be sent to dLazy API and file-hosting endpoints.

Mitigation: Review prompts and file paths before execution, and avoid uploading sensitive, private, or unlicensed media.

Risk: A dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use account controls to rotate or revoke keys as needed, and prefer per-session environment-variable use when persistent local storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured Chinese adaptation sections and inline shell commands when generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are conversation-facing drafts and guidance; image-generation commands may return hosted result URLs from dLazy services.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
