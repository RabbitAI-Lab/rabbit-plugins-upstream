## Description:

Checks EVM, Bitcoin-family, and TRON wallet address formats before transfers and fails when an address does not match supported patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill as a local pre-transfer screening aid for common wallet address formats. It helps flag unsupported or suspicious address strings before a user relies on wallet software or a fuller validator for final confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A PASS result can be mistaken for proof that an address is valid, safe, or correct for a transfer even though the skill performs rough format screening.

Mitigation: Treat PASS as a preliminary signal only; verify the address in wallet software or a validator that performs full checksum and network/version checks before sending funds.

Risk: Installing an unreviewed package can expose users to unexpected behavior in a transfer-related workflow.

Mitigation: Install only from a pinned, reviewed commit or release and review the packaged files before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/wallet-address-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON command output with exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output; returns rc=0 for accepted format, rc=1 for suspicious format, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter and release changelog mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
