## Description:

ppt to video, word to video, excel to video, pdf to video, document to video - parse, outline, storyboard, voiceover, build, validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn presentations, PDFs, spreadsheets, and documents into explainer, report, courseware, or training video workflows through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the third-party dLazy API and file storage services.

Mitigation: Attach only files appropriate for upload to dLazy and review organizational data-handling requirements before use.

Risk: A dLazy API key may be saved in the local CLI configuration.

Mitigation: Use normal local account protections and rotate or revoke the API key from the dLazy dashboard when access should change.

Risk: Global CLI installation persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI run is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Streamed CLI text or Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped dLazy sessions and uploaded user files.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
