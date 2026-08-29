## Description:

Converts documents such as Word, Markdown, PDF, Excel, or PPT files into explainer, report, courseware, or training video workflows through the dLazy hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, educators, and business users use this skill when they want an agent to turn source documents into video-generation workflows for explainers, report broadcasts, courseware, or training materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy hosted services, and attached files may be uploaded to dLazy media storage.

Mitigation: Confirm that the user and organization permit this cloud processing before sending sensitive, regulated, or confidential documents.

Risk: A dLazy API key may be stored locally in the CLI configuration.

Mitigation: Use OS user-level file protections, prefer per-invocation credentials when appropriate, and rotate or revoke the key from the dLazy dashboard if the machine is shared or compromised.

Risk: A global CLI install persists the dLazy binary on the host.

Mitigation: Use the pinned npx invocation when a temporary install is preferred, or review the pinned CLI package before installing it globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the dLazy hosted service; attached local files are uploaded to dLazy media storage before use.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
