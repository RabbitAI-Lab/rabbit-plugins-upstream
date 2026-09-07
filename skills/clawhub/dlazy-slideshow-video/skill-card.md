## Description:

Turns slides or a document into a narrated slideshow-style video with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, educators, and business teams use this skill to turn PPT, PDF, Word, Excel, or similar documents into narrated slideshow, explainer, report, courseware, or training videos through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party npm CLI globally persists executable code on the user's machine.

Mitigation: Prefer the pinned npx invocation when a persistent global binary is not needed, and review the dLazy CLI source or package before installation.

Risk: Attached local files are uploaded to dLazy services for processing.

Mitigation: Attach only files intended for upload and avoid sending sensitive documents unless the user's dLazy organization policies allow it.

Risk: The dLazy API key is stored in the local CLI config or passed through the environment.

Mitigation: Protect ~/.dlazy/config.json with user-only permissions and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and dLazy CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to invoke the pinned dLazy CLI template and may involve uploading user-selected files to dLazy services.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
