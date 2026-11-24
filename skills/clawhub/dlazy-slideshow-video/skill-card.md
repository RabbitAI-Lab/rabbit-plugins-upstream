## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide presentation or document materials and ask the dLazy file-to-video assistant to create narrated slideshow videos for explainers, reports, courses, or training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial; project listing and CLI login steps and some referenced materials were not fully assessed. The scan also flagged hidden whitespace.

Mitigation: Review the project-listing and login steps, inspect the flagged whitespace, and check missing referenced materials before installing.

Risk: Prompts and attached files are sent to dLazy services, and attached files are uploaded to its media storage.

Mitigation: Review your organization's data-sharing requirements before sending prompts or attaching files.

## Reference(s):

- [CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Video files]

**Output Format:** [Markdown responses with inline shell commands and generated slideshow video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn generation; attached files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
