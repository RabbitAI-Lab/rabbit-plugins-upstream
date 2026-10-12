## Description:

Guides Chinese-language adaptation of web novels into episodic webtoon scripts and can generate images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creators use the skill to turn web-novel chapters into plot breakdowns, episode plans, and webtoon scripts, with optional dLazy-powered image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The writing workflow also invokes a dLazy CLI that runs npm/npx commands and sends prompts and potentially local media to external services.

Mitigation: Review the CLI before installation and confirm the exact prompts, files, and commands before generating images.

Risk: Authentication can leave an API key in a persistent local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable if persistent local storage is unwanted; protect and rotate credentials as needed.

Risk: Generated media may be returned as hosted URLs, and the writing and image-generation paths are not clearly separated.

Mitigation: Confirm whether external processing and hosted outputs suit the source material before using image generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image links]

**Output Format:** [Chinese-language Markdown with episodic scripts and optional image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes plot breakdowns, episode tags, and revision guidance.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
