## Description: <br>
Identity Aiops helps agents operate Keycloak or authentik identity providers for user, event, client, MFA, login-failure, stale-access, and governed account or OAuth administration workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Identity, security, and platform operators use this skill to inspect Keycloak or authentik tenants, analyze login failures, stale access, OAuth client configuration, and MFA coverage, and perform audited account or client changes when the connected account is authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact identity and OAuth administration without an in-tool approval gate. <br>
Mitigation: Install it only where agent-driven identity administration is intended, start with view-only Keycloak or authentik permissions, and grant manage-users or manage-clients only for controlled sessions. <br>
Risk: Audit approval environment variables are recorded as annotations but are not enforcement controls. <br>
Mitigation: Use account permissions and the agent's operating instructions as the enforcement layer, and do not rely on approval annotations to block writes. <br>
Risk: Client-secret rotation and session revocation can cause immediate operational impact and may not be reversible. <br>
Mitigation: Use dry runs where available, stage dependent deployments before rotating secrets, and review audit and undo records after state-changing operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/identity-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Identity-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe identity-provider API observations, RCA findings, dry-run write plans, audit implications, and follow-up commands.] <br>

## Skill Version(s): <br>
0.4.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
