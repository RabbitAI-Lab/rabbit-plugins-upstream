## Description:

Turns a script or scene breakdown into a storyboarded, shot-by-shot video through the dLazy storyboard service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn scripts into multi-shot animated videos with storyboards, consistent characters, audio, subtitles, and assembled scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services.

Mitigation: Avoid sensitive prompts or attachments unless sharing them with dLazy is intended.

Risk: Logging in can store a dLazy API key on the local device.

Mitigation: Protect the local key and rotate or revoke it through dLazy if needed.

Risk: Using the skill installs or runs an external CLI.

Mitigation: Review the pinned dLazy CLI before use; use the pinned npx option if a global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text responses with project-based video deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports follow-up work within an existing project.]

## Skill Version(s):

1.0.28 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
