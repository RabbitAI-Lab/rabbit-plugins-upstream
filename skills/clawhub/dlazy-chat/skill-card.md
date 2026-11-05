## Description:

Chat with dLazy’s project-scoped sandbox agent for multi-turn work, and discover available skills and projects through the CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or continue project-scoped conversations with the hosted sandbox agent, select a skill, and provide prompts or attachments for multi-turn work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers could send messages to dLazy or start remote work without a clear request to use that service.

Mitigation: Use explicit dLazy requests or manual activation before starting a chat.

Risk: Messages and selected attachments are sent to dLazy, and remote work can consume credits.

Mitigation: Confirm the target project and attachments before submission, and consider the expected service usage.

Risk: The pinned CLI executable was not bundled or audited with this release evidence.

Mitigation: Review the pinned CLI version and its published source before installation.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Streamed conversational responses, potentially including Markdown and code blocks or generated files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped and multi-turn; the exact output depends on the selected remote skill.]

## Skill Version(s):

1.2.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
