## Description:

Converts documents into explainer, report, courseware, or training video projects by routing the agent through dLazy's file-to-video CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to turn documents such as Word, Markdown, PPT, Excel, or PDF files into explainer, training, courseware, or report-review video projects through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, prompts, and attached files are sent to dLazy services for processing.

Mitigation: Only attach documents approved for third-party SaaS processing, and review dLazy service terms and data handling before use.

Risk: The CLI requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Authenticate only on trusted machines, avoid exposing the key in logs or shared shells, and rotate or revoke the key if exposure is suspected.

Risk: A global npm install leaves a persistent dLazy CLI binary on the system.

Mitigation: Review the @dlazy/cli package or use the pinned npx invocation when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project identifiers, authentication setup steps, file attachment handling, and dLazy service status or error responses.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter lists 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
