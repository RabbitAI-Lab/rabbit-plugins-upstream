## Description:

Helps sales teams find US local-business leads by category and location, with contact details and signals such as website, booking, payment, and hiring status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and agencies use this skill to find and qualify local businesses for outreach, export leads to a CRM, or identify a business by phone number or website.

### Deployment Geography for Use:

United States (currently CA, TX, FL, NY, PA, IL, OH, GA, NC, and DE)

## Known Risks and Mitigations:

Risk: Lead searches are sent to Liquid Agent's API.

Mitigation: Submit only business-search inputs you are comfortable sharing with that service.

Risk: Paid searches can spend USDC through x402.

Mitigation: Check the quoted total and requested lead count before authorizing payment.

Risk: The example command runs an unpinned x402 client through npx.

Mitigation: Prefer a pinned or trusted x402 client instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/leftychris13/skills/liquid-local-leads)
- [Liquid Agent leads API](https://api.liquidagent.ai/v1/leads)
- [Liquid Agent MCP endpoint](https://api.liquidagent.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, CSV, Guidance]

**Output Format:** [Markdown or CSV lead lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead details may include contact information, email grades, and buying signals; CSV export is available.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
