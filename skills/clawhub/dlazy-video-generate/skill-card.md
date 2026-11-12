## Description:

Video generation skill that automatically selects the best dlazy CLI video model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and users of agent assistants use this skill to generate, animate, and edit videos from prompts and reference media, including lip-sync and digital-human workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image, video, or audio files may be sent to dLazy's hosted services for processing.

Mitigation: Avoid submitting sensitive prompts or media, and confirm supplied media is appropriate to upload.

Risk: The skill offers image and speech workflows alongside video generation, and the security scan could not resolve some references.

Mitigation: Check the selected workflow and its referenced CLI behavior before running it, and provide only the intended inputs.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video media, typically returned as hosted URLs, with JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can use supplied image, video, or audio as generation inputs; generated media is hosted by dLazy.]

## Skill Version(s):

1.4.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
