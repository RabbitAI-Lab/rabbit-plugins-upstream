## Description:

Turns a document, topic, or brief into a narrated explainer video by helping outline, storyboard, generate voiceover, build, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn documents, topics, or briefs into narrated explainer, courseware, report, or training videos through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to the external dLazy service, including uploads to files.dlazy.com when --files is used.

Mitigation: Only submit prompts and files intended for upload to dLazy, and avoid attaching confidential documents unless that service use is approved.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use OS-user-restricted configuration, rotate or revoke organization API keys when needed, or provide DLAZY_API_KEY per invocation when local persistence is not desired.

Risk: Installing the CLI globally persists a binary on the system.

Mitigation: Use the pinned npx invocation when a non-persistent execution path is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, prompts, attached files, API authentication, and dLazy service responses.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
