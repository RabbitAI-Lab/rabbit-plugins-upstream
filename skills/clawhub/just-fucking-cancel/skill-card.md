## Description: <br>
Finds unwanted subscriptions by analyzing transaction data, estimating recurring costs, and providing cancellation URLs through CSV-based analysis with optional Plaid integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chipagosfinest](https://clawhub.ai/user/chipagosfinest) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to audit bank transactions for recurring charges, decide which subscriptions to cancel or keep, and receive manual cancellation links and guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial transaction data is sensitive, and optional Plaid mode can transmit transaction data to Plaid. <br>
Mitigation: Prefer CSV mode for local processing; enable Plaid only intentionally and protect, rotate, or remove Plaid credentials and access tokens when needed. <br>
Risk: Broad triggers such as "save money" could activate the skill before the user intends to analyze financial data. <br>
Mitigation: Confirm the user's intent before ingesting transaction data and consider narrowing activation phrases in deployment. <br>
Risk: Cancellation URLs and service-specific guidance can be incomplete or stale. <br>
Mitigation: Treat output as manual guidance, verify cancellation steps with the provider, and keep screenshots or confirmation numbers for difficult cancellations. <br>


## Reference(s): <br>
- [Common Services - Cancellation Guide](references/common-services.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chipagosfinest/skills/just-fucking-cancel) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown conversation output with an HTML audit report and cancellation URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use optional Plaid credentials for transaction retrieval; CSV mode is local processing.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
