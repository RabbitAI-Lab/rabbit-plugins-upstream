## Description:

Sanitize PII/secrets (FEIN, SSN, names, credentials) from text or files with the local ClaimCheck CLI before anything leaves the machine; reversible via the local vault.

This skill is ready for commercial/non-commercial use.

## Publisher:

[normandmickey](https://clawhub.ai/user/normandmickey)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use ClaimCheck to find and replace sensitive values in text or files before sharing them in chats, tickets, documents, or commits. They can restore placeholders locally using the recovery vault.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Windows installation instructions download and execute an installer script.

Mitigation: Review and pin the installer before execution, or build from a verified source revision.

Risk: The recovery vault retains original sensitive values in plaintext on the local machine.

Mitigation: Protect ~/.sanitize-mcp/vaults and treat the machine as the trust boundary.

Risk: Sanitization may miss sensitive values, and runtime privacy was not independently verified.

Mitigation: Inspect sanitized output before sharing and do not assume all sensitive data was removed.

## Reference(s):

- [ClaimCheck homepage](https://claimcheck.saasclaw.ai)
- [ClaimCheck source repository](https://github.com/saasclawai-org/ClaimCheck)
- [Windows installer script](https://raw.githubusercontent.com/saasclawai-org/ClaimCheck/main/tools/install.ps1)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Sanitized text or file findings, including JSON summaries and placeholders; command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stable placeholders can be restored locally from the vault; inspect sanitized output before sharing.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
