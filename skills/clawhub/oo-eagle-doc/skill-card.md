## Description:

Eagle Doc lets an agent operate Eagle Doc through an OOMOL-connected account for usage, quota, request-log, and finance-document OCR actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Eagle Doc action schemas, run account-connected Eagle Doc operations, review usage and quota information, and process finance documents through OCR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run broad account-connected Eagle Doc actions, including finance-document upload.

Mitigation: Inspect the live action schema before execution and confirm the exact payload and expected effect with the user before any write or document-upload action.

Risk: The setup guidance includes installing the oo CLI through remote scripts without bundled integrity checks.

Mitigation: Prefer a verifiable package or documented release source before installing, and review the setup command before execution.

Risk: Finance documents and usage data may be sensitive and tied to the connected OOMOL/Eagle Doc account.

Mitigation: Confirm the account context and document sensitivity before upload or retrieval, and avoid processing documents that should not be shared with the connected service.

## Reference(s):

- [Eagle Doc API product page](https://www.eagle-doc.com/en/products/eagle-doc-apis/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eagle-doc)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs account-connected oo CLI actions after schema inspection; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
