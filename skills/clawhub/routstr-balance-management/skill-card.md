## Description: <br>
Manage Routstr balance by checking balance, creating Lightning invoices for top-up, and checking invoice payment status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sh1ftred](https://clawhub.ai/user/sh1ftred) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Routstr users use this skill to inspect account balance and usage, create Lightning invoices, check invoice status, and top up balance with Cashu tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a Routstr API key and sends balance or top-up requests to the configured base URL. <br>
Mitigation: Confirm ~/.openclaw/openclaw.json points to a trusted HTTPS Routstr endpoint and protect the API key before running the scripts. <br>
Risk: Cashu tokens and Lightning invoices can represent payment value or expose payment material. <br>
Mitigation: Verify invoice amounts and token redemption intent, and avoid pasting Cashu tokens into shared shells, logs, or chat transcripts. <br>
Risk: The security review flagged under-scoped financial-risk behavior. <br>
Mitigation: Install only when you intend to manage and top up a Routstr account from this machine, and review the scripts before use. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Configuration] <br>
**Output Format:** [Shell script output with text summaries and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads Routstr base URL and API key from ~/.openclaw/openclaw.json and accepts amount, invoice ID, or Cashu token arguments depending on the script.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
