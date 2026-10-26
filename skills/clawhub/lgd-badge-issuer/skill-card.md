## Description:

Creates lgd-certified badge certificates and issuance records from supplied evidence labels, with SHA-256 fingerprints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers can generate a local badge certificate and issuance ledger for an LGD three-laws assessment. Verify the assessment independently before using the badge as a credential.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A badge may appear to certify a passed assessment even when supplied evidence has not been authenticated or checked for passing results.

Mitigation: Authenticate the evidence, bind it to the holder, and verify explicit passing results before treating the badge as an authoritative credential.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-issuer)
- [LGD theory background (linked in README)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Console text or JSON, with optional JSON certificate and local JSON issuance ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Certificates include holder, serial, evidence hashes, and a SHA-256 fingerprint; refusals are recorded in the ledger.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
