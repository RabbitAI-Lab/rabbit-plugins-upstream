## Description:

Converts PPT, Word, Excel, PDF, and other documents into videos by parsing content, creating outlines and storyboards, adding voiceover, building the video, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users can use this skill to turn source documents into explainer videos, report broadcasts, courseware, or training videos through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for documents that organizational policy allows to be processed by dLazy's hosted service.

Risk: The dLazy CLI requires an API key that may be stored in a local configuration file or supplied through an environment variable.

Mitigation: Store keys using the documented CLI authentication flow, rotate or revoke keys when needed, and avoid exposing keys in prompts, logs, or shared shell history.

Risk: A global npm installation persists the CLI on the user's system.

Mitigation: Use the documented npx invocation when a temporary, non-persistent CLI run is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded user files and project-scoped chat sessions managed by the dLazy CLI.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
