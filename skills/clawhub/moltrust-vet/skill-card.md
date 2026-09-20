## Description:

Check any agent skill against ten versioned, CWE-mapped security checks before you install it, and get a verdict a third party can recompute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moltycel](https://clawhub.ai/user/moltycel)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security reviewers, and skill publishers use this skill to vet agent skills before installation or release by requesting a reproducible MolTrust audit and reporting the score, findings, auditor version, skill hash, and ecosystem trust score.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository URLs submitted for audit may identify private or sensitive skills if a user provides non-public targets.

Mitigation: Use the skill mainly with public or intentionally shared repository URLs, and avoid submitting confidential targets unless authorized.

Risk: Optional MolTrust identity registration creates a local private key that the user must protect.

Mitigation: Skip identity registration unless a MolTrust author identity is needed, and store any generated private key in approved local secret storage.

Risk: A passing audit reflects ten specific checks over the fetched skill file at that time and is not a complete safety guarantee.

Mitigation: Treat the score and findings as one review input, and combine them with manual review and deployment-specific security checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/moltycel/skills/moltrust-vet)
- [MolTrust skill homepage](https://moltrust.ch/skills.html)
- [MolTrust audit checks API](https://api.moltrust.ch/guard/audit/checks)
- [MolTrust audit version API](https://api.moltrust.ch/guard/audit/version)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with audit score, pass/fail status, findings, auditor version, skill hash, and ecosystem trust score.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include inline HTTP GET examples for audit and verification endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
