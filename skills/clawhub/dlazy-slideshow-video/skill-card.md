## Description:

Turns slides, documents, or images into narrated slideshow-style videos with voiceover and transitions through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert presentations, PDFs, documents, or reference files into narrated explainer, report, courseware, or training videos. Agents use it by starting or continuing dLazy projects with the pinned file-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local files are sent to dLazy services for processing.

Mitigation: Avoid uploading sensitive documents unless dLazy's terms fit the use case and organizational policy.

Risk: The dLazy API key may be stored in a local user configuration file.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local storage is not desired, and rotate or revoke organization-scoped keys from the dLazy dashboard when needed.

Risk: The workflow depends on a third-party hosted service and account balance.

Mitigation: Confirm authentication and available dLazy credits before relying on the skill for time-sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and service-generated media references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI pinned to @dlazy/cli 1.2.3 and the file-to-video template.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
