## Description:

Filters Shopee's T+1 trending-keyword data by category, product location, recent sales, and suggested bid to help users find relevant search terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketing analysts use this skill to find Shopee keywords for a selected site and date, filtering by category, sales, location, and suggested bid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node can change software on the user's machine.

Mitigation: Prefer a preinstalled or pinned qhkit version; allow persistent PATH or shell-profile changes only with the user's approval.

Risk: Local token configuration may expose a credential through shell history.

Mitigation: Avoid typing tokens directly into recorded shell commands and handle credentials securely.

Risk: Qinghu API queries may incur paid credits.

Mitigation: Check the current estimate and obtain the user's consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-keyword-list)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shopee site, date, and sample size accompany figures; paid calls report credits used.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
