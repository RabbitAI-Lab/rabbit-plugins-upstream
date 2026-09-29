## Description:

Screens Chinese-language token whitepapers and disclosures for five required topics and phrases promising returns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Developers and reviewers use this skill to preliminarily check Chinese-language token disclosures for token supply, allocation, lockups, team information, risk notices, and return promises before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword screening can miss misleading disclosures or flag phrases without understanding their context.

Mitigation: Treat results as a preliminary checklist, not legal or investment advice; have a qualified reviewer assess the full disclosure.

Risk: The skill lists broader file-writing and web-access capabilities than its local screening requires.

Mitigation: Grant only local read and execution access when running the checker, rather than broad Write or WebFetch access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/token-disclosure-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text checklist or JSON screening result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports missing topics and return-promise phrase matches; exit status 0 for pass, 1 for fail, or 2 for usage error.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
