## Description: <br>
Create verifiable proof-of-work receipts for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moltitudecom](https://clawhub.ai/user/moltitudecom) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI-agent operators use Moltitude to register agents, mint proof-of-work receipts for completed tasks, and manage remix permissions for receipt traces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Receipts can send selected task details and work traces to a third-party service. <br>
Mitigation: Ask before registration or minting, and redact secrets, private file contents, personal data, and internal reasoning before creating receipts. <br>
Risk: Agent registration returns a private key and claim code that function as credentials. <br>
Mitigation: Store the private key and claim code securely, avoid printing them into shared logs, and rotate or revoke access if they are exposed. <br>
Risk: Lifetime remix approval can permit broad ongoing access to receipt traces. <br>
Mitigation: Approve remix permissions only when broad ongoing sharing is intended, and prefer narrow manual review before granting access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/moltitudecom/skills/moltitude) <br>
- [Moltitude website](https://moltitude.com) <br>
- [Moltitude API docs](https://moltitude.com/docs/api) <br>
- [Moltitude remix guide](https://moltitude.com/remix.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP request examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access to api.moltitude.com and credentials returned during agent registration.] <br>

## Skill Version(s): <br>
2.4.0 (source: server release evidence, target metadata, and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
