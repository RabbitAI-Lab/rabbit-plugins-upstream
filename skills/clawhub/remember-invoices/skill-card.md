## Description: <br>
Billing memory that tracks invoices, payment status, and follow-ups for agents handling billing workflows, with a required BlueColumn API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and billing operations teams use this skill to let an agent record, recall, update, and follow up on invoice status through BlueColumn during billing conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends invoice and billing context to a remote BlueColumn/Supabase API. <br>
Mitigation: Confirm BlueColumn is approved for the organization's billing and customer data before installation. <br>
Risk: Invoice notes may contain unnecessary personal, regulated, banking, or contract-sensitive details. <br>
Mitigation: Limit stored notes to the billing context needed for invoice tracking and follow-up. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/remember-invoices) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with bash code blocks and JSON request payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY and sends billing details to a remote BlueColumn/Supabase API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
