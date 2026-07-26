## Description: <br>
Send USD from one agent to another. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[afeef23](https://clawhub.ai/user/afeef23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents can use this skill to simulate a USD transfer between two agent identifiers and receive a structured result. It should not be treated as a real payment tool without documented provider integration, authentication, confirmation, audit logging, and transfer limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill appears to simulate a USD transfer and does not actually move money or access payment systems. <br>
Mitigation: Treat transfer results as demonstration output until a version documents payment-provider integration and real fund movement. <br>
Risk: A financial-transfer skill can create user harm if sender, recipient, amount, authentication, audit logging, or limits are unclear. <br>
Mitigation: Require explicit user confirmation, authenticated sender and recipient validation, audit logs, and transfer limits before using it with actual funds. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Code] <br>
**Output Format:** [JSON object with success, transaction_id, message, and optional error_code fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts from_agent, to_agent, amount, and optional memo inputs; returns a simulated transfer result.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
