## Description:

Converts documents such as PPT, Word, Excel, PDF, and Markdown into explainer, report, courseware, or training video workflows through the dLazy file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn supplied documents into video projects with outlining, storyboarding, voiceover, generation, and validation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Use the skill only with documents approved for dLazy SaaS processing, and avoid confidential material unless organizational policy permits it.

Risk: Local files attached with the CLI are uploaded to dLazy media storage.

Mitigation: Review attachments before invoking the skill and remove sensitive or unintended files from the command.

Risk: The dLazy API key is stored locally or supplied through the environment.

Mitigation: Protect the local config and environment, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids, uploaded files, authentication setup, and dLazy CLI command output.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
