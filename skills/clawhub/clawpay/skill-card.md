## Description: <br>
Payment requests and delivery for AI agents and humans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kirch](https://clawhub.ai/user/kirch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Clawpay to create paid requests, share pay links, check payment status, and deliver payloads after payment. It supports agent-to-agent and human-to-agent exchanges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment requests may use an incorrect wallet address, amount, currency, pay URL, or request ID. <br>
Mitigation: Confirm payment details before creating, sharing, paying, or delivering a request. <br>
Risk: Heartbeat polling may track or act on requests outside the intended workflow. <br>
Mitigation: Restrict heartbeat checks to request IDs the agent is deliberately tracking. <br>
Risk: Remote installation commands download skill files from the network. <br>
Mitigation: Review downloaded files or use a pinned, verified package source when available. <br>
Risk: Delivery may send unintended payloads to the Clawpay service. <br>
Mitigation: Only deliver payloads that are intended to be sent to Clawpay after confirming payment status. <br>


## Reference(s): <br>
- [Clawpay Skill Page](https://clawhub.ai/kirch/skills/clawpay) <br>
- [Clawpay Homepage](https://clawpay.ai) <br>
- [Clawpay API Base](https://clawpay.ai/v1) <br>
- [Skill Definition](https://clawpay.ai/skill.md) <br>
- [Heartbeat Documentation](https://clawpay.ai/heartbeat.md) <br>
- [Skill Metadata](https://clawpay.ai/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash commands, JSON response examples, URLs, and status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces payment request IDs, pay URLs, status checks, and optional delivery payload guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
