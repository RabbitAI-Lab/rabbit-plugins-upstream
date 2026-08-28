## Description:

Turns a document, topic, or brief into a narrated explainer video by helping outline, storyboard, generate voiceover, build, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create explainer, courseware, report-broadcast, or training videos from documents, topics, or briefs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy services.

Mitigation: Avoid uploading sensitive documents unless dLazy is an acceptable processor for that data.

Risk: Authentication stores a dLazy API key in local CLI configuration when login or auth set is used.

Mitigation: Use OS user protections for the local config, rotate or revoke keys when needed, or supply DLAZY_API_KEY per invocation for less persistence.

Risk: A global CLI install persists the dLazy command on the system.

Mitigation: Use the pinned npx invocation when a persistent global installation is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the dLazy service and may reference generated project outputs or uploaded files.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
