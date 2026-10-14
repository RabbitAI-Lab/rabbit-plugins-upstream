## Description:

Helps users search Chinese procurement notices, assess bids, discover opportunities, and research companies using the ZLBX service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales teams use this skill to find tenders and early opportunities, assess whether to bid, and review customers, suppliers, and competitors. It can also check the user's ZLBX account balance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags hidden comment-based request and update instructions for review.

Mitigation: Review the skill's request and update behavior before installation and approve only the actions you expect.

Risk: The skill uses a persistent API key, including one stored in ~/.zlbx/config.json after registration.

Mitigation: Protect the key and local config file, and avoid exposing credentials in prompts or shared reports.

Risk: Optional auto-registration sends operating system, CPU architecture, and a hashed MAC address to the service.

Mitigation: Review this data sharing before consenting; configure your own API key to skip auto-registration.

Risk: Generated direct-access sk links may grant access without a normal login.

Mitigation: Do not share generated links or reports broadly unless recipients should have that access.

Risk: Data requests can consume paid credits.

Mitigation: Agree on the scope of searches and analyses before issuing chargeable requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Tender search overview](references/tender-search/overview.md)
- [Bid decision overview](references/bid-decision/overview.md)
- [Opportunity radar overview](references/opportunity-radar/overview.md)
- [Company intelligence overview](references/company-intel/overview.md)
- [Registration and privacy details](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Reports]

**Output Format:** [Text and Markdown reports, with optional HTML report exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include procurement links and cited ZLBX data; some queries consume paid credits.]

## Skill Version(s):

1.1.4 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
