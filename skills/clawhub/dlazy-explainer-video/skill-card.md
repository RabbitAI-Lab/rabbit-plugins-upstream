## Description:

Turns documents, topics, or briefs into narrated explainer, courseware, or training videos through outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to create narrated explainer or training videos from documents, reports, topics, or briefs by invoking the dLazy CLI-backed hosted video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages and attached files are sent to dLazy's hosted API and storage.

Mitigation: Use the skill only with documents that are appropriate to send to dLazy's hosted service.

Risk: An API key may be saved in the local dLazy CLI configuration.

Mitigation: Use the documented dLazy authentication flow and rotate or revoke the key from dLazy when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, prompts, local file attachments, API-key setup, and hosted dLazy service responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
