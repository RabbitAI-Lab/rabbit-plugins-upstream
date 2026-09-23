## Description:

Converts documents such as Word, Markdown, PPT, Excel, and PDF files into explainer, report, courseware, or training videos through the dLazy hosted document-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and business users use this skill to start or continue dLazy document-to-video projects from local documents, prompts, and project IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly attached with --files are sent to the dLazy hosted service.

Mitigation: Review documents for sensitive content before upload and use the skill only with files appropriate for the dLazy service.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use the pinned npx invocation when avoiding a persistent global install, and rotate or revoke the dLazy API key when access requirements change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI invocation and may reference dLazy project IDs, local file attachments, and API-key authentication.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
