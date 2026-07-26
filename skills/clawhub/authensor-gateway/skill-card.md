## Description: <br>
Authensor Gateway is a fail-safe policy gate for OpenClaw marketplace skills that checks tool-call metadata against Authensor policy before execution, allows low-risk actions, requires approval for high-risk actions, and blocks dangerous actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[authensor](https://clawhub.ai/user/authensor) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to mediate OpenClaw marketplace skill tool calls through an external Authensor policy service before execution, with approval and audit receipts for higher-risk actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on an external Authensor control plane to make allow, deny, and approval decisions for tool calls. <br>
Mitigation: Verify CONTROL_PLANE_URL before use, use a dedicated Authensor API key, and confirm the fail-closed behavior matches the deployment's availability requirements. <br>
Risk: File paths and action metadata may be recorded as policy receipts by the external service. <br>
Mitigation: Review the retention and audit requirements before deployment and avoid using the gateway where action metadata disclosure is unacceptable. <br>
Risk: Prompt-level enforcement is advisory when the code-level PreToolUse hook is not enabled. <br>
Mitigation: Enable the authensor-gate.sh hook where stronger enforcement is required and review policies for high-risk command patterns such as download-and-execute workflows. <br>


## Reference(s): <br>
- [Authensor for OpenClaw](https://github.com/AUTHENSOR/Authensor-for-OpenClaw) <br>
- [Authensor Gateway Marketplace Listing](https://www.clawhub.ai/AUTHENSOR/authensor-gateway) <br>
- [Authensor Gateway Skill Page](https://clawhub.ai/authensor/skills/authensor-gateway) <br>
- [ClawHavoc threat report](https://snyk.io/blog/clawhavoc) <br>
- [OpenClaw Docker security documentation](https://docs.openclaw.ai/gateway/security) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only skill; requires CONTROL_PLANE_URL and AUTHENSOR_API_KEY and sends redacted action metadata to the control plane.] <br>

## Skill Version(s): <br>
0.7.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
