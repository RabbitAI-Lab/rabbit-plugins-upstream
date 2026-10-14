## Description:

Helps agents find US local-business leads by location and category, with contact details and buying signals from Liquid Leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and agents use this skill to find and export local-business prospects, check contact and website signals, and look up businesses by phone or domain.

### Deployment Geography for Use:

United States; documented coverage: CA, TX, FL, NY, PA, IL, OH, GA, NC, and DE.

## Known Risks and Mitigations:

Risk: Paid lead searches and lookups can incur USDC charges.

Mitigation: Confirm search terms and the quoted x402 price before authorizing payment; use free count or sample requests first.

Risk: Exported contact information may be used for non-compliant outreach or retained improperly.

Mitigation: Apply applicable privacy, marketing, and platform rules to outreach and data retention.

Risk: The paid example runs an unpinned npm client through npx.

Mitigation: Use a trusted or pinned x402 client rather than blindly running the latest package.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/leftychris13/skills/liquid-local-leads)
- [Liquid Leads API](https://api.liquidagent.ai/v1/leads)

## Skill Output:

**Output Type(s):** [Text, Shell commands, CSV]

**Output Format:** [Markdown guidance and shell commands; CSV for exported leads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches can return graded emails, business contact details, and buying signals; paid requests use x402.]

## Skill Version(s):

1.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
