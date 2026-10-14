## Description:

Chat with dLazy's hosted sandbox agent across project-based, multi-turn tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can discover dLazy skills and projects, start a hosted sandbox-agent conversation, and continue work across turns with optional file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers may send prompts or attached files to dLazy using a stored API key without a clear request for that service.

Mitigation: Invoke only for explicit dLazy commands or product-specific requests; treat prompts and files attached with --files as data sent to dLazy.

Risk: Installing the external CLI and retaining its API key expose users to third-party software and account access risks.

Mitigation: Review the @dlazy/cli package before global installation and rotate or revoke the dLazy API key when no longer needed.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Conversational text; format depends on the selected dLazy skill]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses stream from the hosted agent and can retain project context across turns.]

## Skill Version(s):

1.2.31 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
