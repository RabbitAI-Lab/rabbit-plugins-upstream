## Description:

Analyzes construction-sector tender and bid data from the 知了标讯/建设通 workflow, focusing on project value, winning bidder background, qualifications, and performance summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Chinese construction project tenders, inspect bidder and supplier records, compare company bidding activity, and summarize market or project performance from the vendor API.

### Deployment Geography for Use:

Global; source data and workflows are focused on Chinese tender and procurement records.

## Known Risks and Mitigations:

Risk: The optional trial registration flow sends a stable MAC-derived hash and device metadata to the vendor.

Mitigation: Prefer a manually provisioned API key when possible; if auto-registration is used, require explicit user consent before collecting or sending device features.

Risk: The workflow may store a vendor API key in ~/.zlbx/config.json.

Mitigation: Use the ZLBX_API_KEY environment variable for managed deployments or protect ~/.zlbx/config.json with restrictive local file permissions.

Risk: Contact lookup features may display contact data returned by the service.

Mitigation: Display contact fields only as returned by the API, respect masked contact responses, and avoid enriching or batch-exporting contact details.

Risk: The skill can add vendor registration, recharge, or referral links during account-related flows.

Mitigation: Keep vendor links clearly tied to account setup or quota recovery and avoid presenting them as neutral documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Publisher profile: pkuycl](https://clawhub.ai/user/pkuycl)
- [Skill definition](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration workflow](artifact/references/auto-register.md)
- [Vendor data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Vendor account and registration service](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON request examples, REST API guidance, and shell commands when local configuration or registration is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY environment variable or local ~/.zlbx/config.json API key; optional account registration stores a vendor API key locally after user consent.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
