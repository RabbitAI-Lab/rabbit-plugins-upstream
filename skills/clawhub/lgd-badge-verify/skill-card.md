## Description:

lgd-badge-verify helps verify LGD badge certificates by recomputing certificate fingerprints, checking evidence-hash fields, and comparing serials and fingerprints against a supplied registry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and governance operators use this skill to check LGD badge certificate integrity and compare certificates with a trusted registry before accepting badge claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A badge certificate can appear verified when it is self-consistent but no authoritative registry, revocation status, or evidence-hash validation is supplied.

Mitigation: Require a trusted registry for trust decisions and independently validate revocation status and evidence hashes.

Risk: A successful verification result could be overused as compliance, access, or trust approval.

Mitigation: Treat results as integrity-checking signals and require human or organizational review for regulated, access-control, or compliance decisions.

Risk: Installing or running an unreviewed release can expose users to changed verifier behavior.

Mitigation: Use a pinned, reviewed source and run the verifier locally or in an isolated environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-verify)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON verification results with process exit codes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local command-line output; registry cross-checking depends on a trusted registry supplied by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
