## Description:

Turns supplied copy into shot-by-shot short-video storyboards, with additional dLazy CLI media-generation instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and production teams use this skill to turn themes, outlines, or supplied copy into shot-by-shot scripts with scene, camera, and spoken-line guidance. Its additional workflow can generate images through dLazy services after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The text-storyboard listing also instructs the agent to install and run a media-generation CLI.

Mitigation: Review the full workflow and only run npm/npx commands with explicit user approval; use the text-only storyboard path when media generation is unnecessary.

Risk: CLI authentication stores a dLazy API key locally.

Mitigation: Use a dedicated, limited-scope key where available, protect local credentials, and rotate or revoke the key if exposed.

Risk: Prompts and provided media may be sent to dLazy services, and generated assets may be returned as hosted URLs.

Mitigation: Avoid sending sensitive copy or private media without consent, and review sharing implications before distributing hosted URLs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI repository (linked in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Hosted image URLs]

**Output Format:** [Markdown storyboard with video settings and shot-by-shot spoken lines; optional CLI commands and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests verbatim preservation of supplied spoken copy; defaults to a 9:16 aspect ratio and 720p resolution.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
