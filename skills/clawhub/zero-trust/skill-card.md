## Description: <br>
Security-first behavioral guidelines for cautious agent operation involving external resources, installations, credentials, or actions with external effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doonot](https://clawhub.ai/user/doonot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and their operators use this skill as a conservative safety protocol for high-risk actions such as link handling, package installation, credential handling, external API calls, messages, financial transactions, and form submissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The approval flow may interrupt work frequently because it requires explicit approval for many external or irreversible actions. <br>
Mitigation: Use it when a conservative safety posture is desired, and document which known low-risk actions remain allowed without approval. <br>
Risk: The artifact names a specific approver, Pat, which may be incorrect in shared or transferred environments. <br>
Mitigation: Before deployment, replace the approval authority language with the current authorized user or designated approver. <br>


## Reference(s): <br>
- [Zero Trust on ClawHub](https://clawhub.ai/doonot/skills/zero-trust) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance and approval-check procedures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No tool calls, scripts, or external API operations are produced by the skill itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
