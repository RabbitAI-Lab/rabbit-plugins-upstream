## Description:

Provides a six-point self-check before interacting with smart contracts, covering audits, contract addresses, token approvals, revocation, private-key safety, and small test transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and other smart-contract users can check six basic precautions before a transaction and identify unanswered checks or unlimited approvals. It is a screening aid, not legal, investment, or smart-contract security advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares web access and file-writing tools beyond those needed for its local checklist.

Mitigation: Run the local Python script directly or restrict WebFetch and Write unless those capabilities are needed.

Risk: Self-reported checklist completion can be mistaken for an independent contract audit or professional advice.

Mitigation: Verify contract details independently and seek qualified legal, investment, or security advice before consequential transactions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/contract-interact-checklist)
- [Publisher project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text checklist or JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists six checks and missing items; reports PASS or FAIL with exit status 0 or 1, or 2 for usage errors.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled skill frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
