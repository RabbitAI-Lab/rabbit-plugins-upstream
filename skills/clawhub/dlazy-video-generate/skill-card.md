## Description:

Selects a dLazy video model to generate or edit video from text, images, or reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose a video-generation model and produce clips from prompts, images, reference media, or talking-head audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images, video, or audio may be uploaded to dLazy's cloud service.

Mitigation: Obtain consent and avoid submitting sensitive media or prompts unless the service is approved for them.

Risk: Generation may consume paid credits, and authentication may store an API key locally.

Mitigation: Confirm expected spending, protect or revoke the key as needed, and use on-demand CLI installation if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with CLI commands and generated video links; CLI responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a dLazy account, API key, and sufficient credits.]

## Skill Version(s):

1.4.30 (source: server release metadata; bundled SKILL.md frontmatter says 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
