## Description:

Checks the order, subject consistency, and linked hash values of electronic evidence-chain entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and compliance reviewers can use this skill to flag ordering, subject, and hash-link inconsistencies in electronic evidence chains. Its findings support human review rather than determining legal admissibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A consistency check could be mistaken for legal advice or proof that evidence is admissible.

Mitigation: Treat results as auxiliary checks and have qualified reviewers assess evidence and current legal requirements.

Risk: Installing from a remote source may execute code that differs from this reviewed release.

Mitigation: Review the remote source and pin the intended version before installing with npx or git.

Risk: Assuming MIT terms cover the accompanying documentation could lead to unauthorized redistribution.

Mitigation: Check the package's separate code and documentation terms before reuse or redistribution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-check)
- [Publisher project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Plain text or structured JSON check results, with optional usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Check results include chain breaks and a completeness flag; exit codes indicate pass, detected issues, or usage error.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
