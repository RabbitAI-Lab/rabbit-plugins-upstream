## Description:

Checks LGD badge certificate fields and fingerprints, with optional matching against an issuer registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and auditors use this skill to check a badge certificate's required fields and fingerprint, and optionally compare its serial and fingerprint with an issuer registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A forged but internally consistent certificate may pass without a trusted registry.

Mitigation: Require a trusted issuer registry or another independent authenticity check before relying on a passing result.

Risk: Ledger access credentials may be exposed during verification.

Mitigation: Use read-only, least-privilege credentials through approved secret handling; do not paste them into prompts, files, or logs.

## Reference(s):

- [LGD Badge Verifier on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-verify)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text or JSON verification result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an overall pass/fail result and individual checks; registry matching is optional.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
