## Description:

Helps sales teams find, preview, export, and enrich U.S. small-business leads and manage related searches, billing, email schedules, and CRM integrations through SMB Sales Boost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomsonx232](https://clawhub.ai/user/tomsonx232)

### License/Terms of Use:

MIT

## Use Case:

Sales teams use this skill to identify U.S. small businesses with recent buying signals, export or enrich lead lists, and manage outreach workflows and CRM connections. Account access is required for most operations.

### Deployment Geography for Use:

Global (U.S. business leads only)

## Known Risks and Mitigations:

Risk: Lead searches, exports, and enrichments may consume credits; purchases, plan changes, auto top-up, and overage billing may charge money.

Mitigation: Get explicit approval before spending or changing billing settings, and set maxCredits on searches and exports.

Risk: Exports and automated CRM or webhook integrations may expose business contact details to third parties.

Mitigation: Confirm recipients and destinations before enabling delivery, and store exported lead files and webhook secrets securely.

Risk: An exposed API key could grant access to the user's SMB Sales Boost account.

Mitigation: Keep the key in the environment and never paste it into chat or shared files.

## Reference(s):

- [SMB Sales Boost](https://smbsalesboost.com)
- [SMB Sales Boost on ClawHub](https://clawhub.ai/tomsonx232/skills/smb-sales-boost-skill)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [Markdown or JSON responses; CSV, JSON, or XLSX lead exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exported leads can include business contact details.]

## Skill Version(s):

1.9.3 (source: server release metadata and bundled script)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
