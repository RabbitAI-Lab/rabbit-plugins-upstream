## Description: <br>
Lends or rents out a logged-in Claude Code or Codex agent through SettleMesh with metered access, allowlists or friend access, and sandbox guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers who intentionally want to share or monetize a logged-in local coding-agent session use this skill to configure SettleMesh lending, access controls, metering, invocation, and sandbox expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Allowed remote callers can drive a live logged-in coding-agent session, and injected login material may be readable by prompts. <br>
Mitigation: Use a narrow allowlist or trusted friends only, never public offers, and revoke cached sessions when lending stops. <br>
Risk: Running without a filesystem-confining sandbox can expose host secrets and the injected login. <br>
Mitigation: Verify sandbox enforcement before lending and avoid the no-sandbox override. <br>
Risk: The skill enables paid credential-lending and metered remote access to local compute. <br>
Mitigation: Require explicit human confirmation for credential-lending or spending actions and confirm pricing and access controls before starting the worker. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/structureintelligence/skills/rent-a-logged-in-agent) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY for authenticated SettleMesh access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
