## Description:

Turns PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos through dLazy's hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, developers, and content teams use this skill when they have a document and need an agent to help create an explainer video, report broadcast, courseware, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are processed by dLazy's hosted service.

Mitigation: Use the skill only for documents that the user is permitted to send to dLazy, and avoid uploading confidential files unless that use is approved.

Risk: Attached local files are uploaded to dLazy media storage before the agent can use them.

Mitigation: Review file contents before attaching them and remove sensitive or unnecessary data before upload.

Risk: The skill uses an API key saved in local CLI configuration or supplied through an environment variable.

Mitigation: Use per-user credentials, restrict local config permissions, and rotate or revoke the dLazy API key if exposure is suspected.

Risk: A global CLI installation persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a temporary install is preferred, or review the CLI source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use the pinned @dlazy/cli package and may involve uploading user-provided files to dLazy services.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
