## Description: <br>
Constrained autonomous delegate for identity-proxied communication that handles incoming messages across email, Discord, Slack, and WhatsApp by analyzing intent and applying declarative authority policies before generating responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sieershafilone](https://clawhub.ai/user/sieershafilone) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and operators use this skill to prototype a policy-bounded communication delegate that can draft, send, block, or escalate messages while preserving user-defined authority limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act as the user across communication channels by drafting, sending, or blocking messages. <br>
Mitigation: Prefer draft-only operation at first, restrict connected channels and trusted contacts, and require explicit review before enabling autonomous send behavior. <br>
Risk: The skill stores local communication, audit, memory, and style data that may include sensitive message context. <br>
Mitigation: Confirm redaction, retention, and deletion controls before real-account use, and avoid connecting sensitive channels until those controls are verified. <br>
Risk: Safety verification is incomplete in the artifact implementation. <br>
Mitigation: Verify that final policy, confidence, and response verifier checks are implemented and tested before using the skill for sensitive or high-stakes communication. <br>
Risk: Watermarking behavior may alter outgoing messages in ways recipients do not expect. <br>
Mitigation: Disable watermarking or make it explicit in user policy before enabling outbound message sending. <br>


## Reference(s): <br>
- [Agent Doppelgänger specification](references/specification.md) <br>
- [ClawHub skill page](https://clawhub.ai/sieershafilone/skills/agent-doppelganger) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code and YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled scripts may create local JSONL audit logs and style or policy files under the configured ADG directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
