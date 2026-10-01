## Description:

Helps adapt web novels into Chinese-language webtoon plot outlines, episode plans, and scripts, with an optional dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creative teams use this skill to turn web-novel chapters into Chinese-language webtoon plot breakdowns, episode tags, and visual scripts. When images are requested, it also guides generation through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-generation workflow installs and runs a third-party CLI.

Mitigation: Review the npm package and dLazy service before use; consider the listed npx alternative rather than a persistent global installation.

Risk: CLI login may store an API key in local configuration.

Mitigation: Use an environment variable if persistent key storage is undesirable, and keep credentials private.

Risk: Local media supplied for image generation may be uploaded to dLazy.

Mitigation: Provide local media paths only when upload to the service is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Chinese-language Markdown outlines and scripts; optional CLI commands and hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are staged in conversation, with episode-by-episode revisions.]

## Skill Version(s):

1.3.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
