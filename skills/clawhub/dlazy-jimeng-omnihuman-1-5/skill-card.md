## Description:

Generates digital-human broadcast videos from portrait images and audio or text with Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human videos from a portrait and audio or text through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media, prompts, and generated outputs are sent to third-party dLazy services.

Mitigation: Review the media and prompts for sensitivity before submitting them to dLazy.

Risk: Authentication can store an API key locally, and installing the CLI adds third-party software.

Mitigation: Review the package before installation; use npx or DLAZY_API_KEY for less persistent local setup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can be downloaded locally when requested.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
