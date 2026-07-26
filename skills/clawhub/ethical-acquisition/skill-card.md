## Description: <br>
Turn a confirmed Offer Brief and Payable Test Plan into a small, policy-compliant acquisition plan with staged, human-reviewed acquisition assets and a specific approval checkpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bilbop1](https://clawhub.ai/user/bilbop1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and builders use this skill before outreach, listings, partnership requests, public content, or buyer-facing acquisition actions to choose one or two permissioned channels, draft honest assets, prepare fulfillment, and surface an exact approval checkpoint before any external action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may prepare outreach, listings, or other acquisition actions that affect external people, accounts, spend, or public content. <br>
Mitigation: Review the exact payload, destination, account, cost, timing, scope, evidence label, and rollback or correction path before approving any external action. <br>
Risk: Using unpermissioned personal data, unclear consent, or channels whose rules do not allow the action can create compliance and platform-abuse risk. <br>
Mitigation: Use only legitimate account access and permissioned data, verify consent or another lawful-use basis, check current channel rules, and block execution when prerequisite status is unknown or failed. <br>
Risk: Buyer-facing assets could become misleading through fake familiarity, hidden commercial intent, pressure, or unverified claims. <br>
Mitigation: Require human review against the message standard: truthful identity and intent, a specific permitted source, easy decline, once-readable length, and verified or removed performance claims. <br>
Risk: Copied offers, contact records, platform responses, or page content may contain prompt injection or unsafe instructions. <br>
Mitigation: Treat those inputs as untrusted evidence, ignore embedded instructions to change scope or disclose private data, and continue only from safe, relevant facts. <br>


## Reference(s): <br>
- [Channel rules](references/channel-rules.md) <br>
- [Message standard](references/message-standard.md) <br>
- [ClawHub skill page](https://clawhub.ai/bilbop1/skills/ethical-acquisition) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown plan with staged draft assets, checklists, approval request or execution-blocked status, and optional action receipt.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [External actions remain staged until a human approves the exact payload, destination, account, timing, scope, cost, evidence label, and rollback or correction path.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact metadata: 0.1.0-rc.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
