## Description: <br>
Pre-send verification for outbound agents: a small, separate guardian placed in front of send() so every email, social post, helpdesk reply, or other outbound message receives an independent verdict across deterministic gates plus an optional LLM semantic check, with a per-message audit log. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to add an independent pre-send control to outbound agent workflows, especially when messages need policy checks, confidential-term screening, claim review, and auditable verdicts before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit results and redlist entries may contain sensitive operational or customer data. <br>
Mitigation: Decide where audit results are stored before deployment and restrict the redlist file to approved, least-privilege locations. <br>
Risk: The optional LLM check can send message body, subject, recipient, and campaign data to the configured model provider. <br>
Mitigation: Use an approved provider or local model, and configure prompts and data handling according to the organization's privacy and compliance requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workloftai/skills/agent-verifier) <br>
- [Workloft Research Note No. 05 - Pre-send verification](https://workloft.ai/labs/notes/pre-send-verifier-2026-05-09.html) <br>
- [Workloft Labs](https://workloft.ai/labs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples and JSON-serializable verification results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces PASS, WARN, or BLOCK verdicts with per-axis checks, optional claim review details, and audit-log data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact package/frontmatter version 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
