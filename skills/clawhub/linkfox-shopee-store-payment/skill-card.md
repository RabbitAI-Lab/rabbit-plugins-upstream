## Description: <br>
Provides agent-facing commands and Python helpers for querying authorized Shopee store payment, escrow, payout, wallet, income report, and installment APIs through LinkFox. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopee merchants and operators use this skill to retrieve settlement, escrow, payout, wallet transaction, income report, and installment-payment data for an already-authorized Shopee store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive Shopee merchant payment and settlement data and saves full API responses locally. <br>
Mitigation: Run it only in protected workspaces, review where the linkfox output directory is created, and remove or restrict access to saved financial JSON files when they are no longer needed. <br>
Risk: The skill uses LinkFox API credentials and authorized Shopee store access to query merchant payment data. <br>
Mitigation: Limit use to stores the user is authorized to access and protect LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY values from logs, shared shells, and committed files. <br>
Risk: The skill may send feedback to LinkFox automatically when behavior, results, or user sentiment indicate a reportable event. <br>
Mitigation: Review feedback behavior before installation and avoid including sensitive merchant financial details in any feedback content. <br>


## Reference(s): <br>
- [Shopee payment API reference](references/api.md) <br>
- [Shopee Open Platform Payment module](https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-payment) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, files, guidance] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries depending on response size.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are persisted under a linkfox session data directory; --inline prints full responses to stdout.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
