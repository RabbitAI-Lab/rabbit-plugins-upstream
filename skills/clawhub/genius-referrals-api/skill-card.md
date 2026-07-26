## Description: <br>
Inspect and manage Genius Referrals accounts, advocates, campaigns, bonuses, redemption requests, and reports through the public Genius Referrals API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alainhl](https://clawhub.ai/user/alainhl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and growth operations teams use this skill to inspect Genius Referrals program data, test API authentication, and perform user-approved account, advocate, referral, bonus, redemption, payout, and reporting actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform mutating Genius Referrals API calls that affect advocates, bonuses, redemption requests, payouts, and deletes. <br>
Mitigation: Default to read-only work, prepare a dry-run summary for writes, and require explicit approval for production writes, payouts, redemption changes, forced bonuses, and deletes. <br>
Risk: API tokens grant access to Genius Referrals account data and actions. <br>
Mitigation: Use GR_API_TOKEN or another user-approved credential source, never place tokens in URLs, prefer scoped tokens where possible, and confirm base URL and account slug before writes. <br>


## Reference(s): <br>
- [Genius Referrals API Documentation](https://api.geniusreferrals.com/doc) <br>
- [Endpoint Catalog](references/endpoint-catalog.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/alainhl/skills/genius-referrals-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with inline API paths, JSON payload notes, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the Genius Referrals API through a local Python helper when the user provides credentials and approval.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
