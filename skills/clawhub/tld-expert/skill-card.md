## Description:

Helps people choose domain endings, check registration availability, and compare current registration and renewal prices using tld.expert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bill-makes](https://clawhub.ai/user/bill-makes)

### License/Terms of Use:

MIT-0

## Use Case:

People naming a product, business, or brand use this skill to compare domain endings, check candidate domains, and review registration and renewal prices before choosing. It can also check whether a name appears in selected public sources, with results treated as pointers rather than legal clearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Naming briefs and candidate domains are sent to tld.expert, and availability checks may involve registrars.

Mitigation: Use nonconfidential naming briefs; for unreleased plans, check only selected domain names.

Risk: External service internals and data retention are outside the inspected package, and listed prices may change.

Mitigation: Confirm current registration and renewal prices with the registrar before purchasing.

## Reference(s):

- [tld.expert](https://tld.expert)
- [tld.expert API specification](https://tld.expert/openapi.json)
- [tld.expert MCP endpoint](https://tld.expert/mcp)
- [Renewal traps snapshot](https://github.com/LeftwayAI/skills/blob/main/skills/tld-expert/references/renewal-traps.md)
- [ClawHub release page](https://clawhub.ai/bill-makes/skills/tld-expert)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with domain availability findings, price comparisons, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include checked candidate domains, dated price information, and recommendations grounded in linked sources.]

## Skill Version(s):

1.1.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
