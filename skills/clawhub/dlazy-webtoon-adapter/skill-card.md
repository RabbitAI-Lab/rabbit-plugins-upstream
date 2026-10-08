## Description:

Helps creators adapt web novels into Chinese-language webtoon plot breakdowns, episode plans, and scripts, with optional dLazy-powered image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use this skill to turn supplied web-novel chapters into plot breakdowns, episode outlines, and visual-first scripts. Optional image generation uses the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the dLazy CLI adds executable third-party software.

Mitigation: Install only if image generation is needed; review the CLI package and linked source before running it.

Risk: Login can store a dLazy API key on disk.

Mitigation: Use DLAZY_API_KEY for nonpersistent credentials; rotate or revoke keys if exposed.

Risk: Prompts and selected media files may be sent to dLazy services.

Mitigation: Review prompts and media paths before generation; avoid sending sensitive material.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image links]

**Output Format:** [Chinese-language structured text and Markdown; optional CLI commands and generated image URLs]

**Output Parameters:** [1D text, with optional links to generated images]

**Other Properties Related to Output:** [Plot breakdowns, episode tags, and scripts are presented in the conversation.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
