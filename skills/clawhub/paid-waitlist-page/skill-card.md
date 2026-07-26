## Description: <br>
Spin up a hosted waitlist, landing, or pre-order page that persists signups to a managed database and can optionally take payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to deploy a hosted waitlist, signup, landing, coming-soon, pre-order, or paywall page with persistent email capture and optional checkout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can deploy a real hosted page, create managed infrastructure, and use metered SettleMesh services. <br>
Mitigation: Review deployment, payment, and credit-spending confirmations before approving them, and use it only when a live hosted waitlist or paid access flow is intended. <br>
Risk: The skill requires SettleMesh authentication through SETTLE_API_KEY or a cached login session. <br>
Mitigation: Provide credentials only in trusted environments and avoid sharing the API key or cached session with untrusted agents or projects. <br>


## Reference(s): <br>
- [Paid Waitlist Page on ClawHub](https://clawhub.ai/structureintelligence/skills/paid-waitlist-page) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and implementation snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce deployment commands and configuration that use settlemesh with SETTLE_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
