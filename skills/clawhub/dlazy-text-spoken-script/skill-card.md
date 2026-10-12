## Description:

Guides agents to write conversational short-video spoken scripts using a seven-part story structure, while also including a separate dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to draft short-video voiceover scripts, character stories, and personal-brand viewpoints. It also describes an optional dLazy image-generation workflow that goes beyond script writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unrelated image-generation workflow may run terminal commands and send prompts or selected media to dLazy services.

Mitigation: Use the script-writing portion alone unless image generation is intended; review commands and media before approving any upload.

Risk: The image workflow may request and store a dLazy API key.

Mitigation: Only configure a key when the image workflow is needed, and review where credentials are stored.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Image links]

**Output Format:** [Markdown prose with optional shell commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven-part spoken script; image-generation steps require separate confirmation.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
