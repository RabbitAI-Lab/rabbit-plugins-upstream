## Description:

Checks token whitepaper or disclosure text for required elements such as total supply, allocation, lock-up, team information, and risk warnings, and fails text that contains promised-return claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance reviewers, and token project teams use this skill to run a local preliminary disclosure completeness check before human legal or investment review. It is a screening aid and does not replace official regulatory guidance or qualified professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions include an unpinned global remote installer that could install unreviewed code.

Mitigation: Install only from a pinned, reviewed release or commit and avoid the unpinned global npx command.

Risk: The checker may be mistaken for legal or investment advice.

Mitigation: Treat results as preliminary screening only and route important decisions to qualified professional review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/token-disclosure-check)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [CLI text or JSON results with deterministic exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns rc=0 for PASS, rc=1 for FAIL, and rc=2 for usage errors.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
