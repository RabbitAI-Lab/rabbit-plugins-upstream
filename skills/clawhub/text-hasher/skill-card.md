## Description:

Compute SHA-256 or MD5 hashes of text strings. Useful for quick integrity checks, deduplication, and content fingerprinting without leaving the terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and terminal users use this skill to generate hashes for copied text, downloaded content, deduplication, and quick equality checks without sending data to a remote service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MD5 hashes are unsuitable for security-sensitive integrity checks.

Mitigation: Prefer SHA-256 for security-sensitive checks and use MD5 only for non-security fingerprints or compatibility.

Risk: Literal text passed through shell commands can be captured in shell history or logs.

Mitigation: Avoid placing sensitive text directly in commands; pipe from controlled input when sensitive data handling matters.

## Reference(s):

- [text-hasher ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/text-hasher)
- [terrycarter1985 ClawHub publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local terminal commands for SHA-256 and MD5 hashing; no network access is required.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
