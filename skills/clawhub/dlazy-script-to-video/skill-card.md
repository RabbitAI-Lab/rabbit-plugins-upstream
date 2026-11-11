## Description:

Turns a script or scene breakdown into a shot-by-shot storyboard and video workflow, from scene breakdown and shot generation through assembly and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video production teams use this skill to turn a script or scene breakdown into a storyboarded, shot-by-shot video, including generated shots, audio, subtitles, and final assembly. It uses the dLazy hosted service and requires a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to the dLazy API, and files attached to a chat are uploaded to dLazy media storage.

Mitigation: Only send prompts and attach files that you are comfortable sharing with the hosted service.

Risk: The skill depends on a pinned third-party CLI, and the supplied security assessment notes a partial scan and some uncertainty.

Mitigation: Review the pinned CLI and confirm its login, project-listing, API, and upload behavior meets your needs before installing or using it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Video files, Storyboard, Text]

**Output Format:** [Rendered video media with storyboard and chat responses; exact media formats depend on the dLazy service output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Files attached to a chat are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
