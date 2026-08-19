## Description:

Compute file checksums (MD5, SHA-1, SHA-256) and verify file integrity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operators use this skill to compute MD5, SHA-1, or SHA-256 checksums for local files and compare expected hashes when checking integrity, duplicates, or digital asset identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MD5 and SHA-1 are legacy hash algorithms and should not be treated as strong security validation.

Mitigation: Use SHA-256 for integrity checks when possible, and reserve MD5 or SHA-1 for compatibility with existing published hashes.

Risk: Checksum scripts operate on local file paths supplied by the user.

Mitigation: Run the scripts only on files intentionally selected for checksum work.

## Reference(s):

- [ClawHub skill page: file-hasher](https://clawhub.ai/terrycarter1985/skills/file-hasher)
- [ClawHub publisher profile: terrycarter1985](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with bash commands and checksum strings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local command-line checksum utilities and returns hash strings or match/mismatch status.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
