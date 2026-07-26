## Description: <br>
Endpoint Aiops helps agents triage and operate managed-endpoint fleets with health, inventory, login-storm, drift, patch, profile-assignment, reboot, audit, budget, and undo workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, IT operators, and endpoint administrators use this skill to inspect managed-endpoint fleet health, diagnose login storms and drift, rank endpoint risk, and perform guarded remediation such as profile assignment or reboot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or reboot managed endpoints and has no enforced read-only or approval gate for agent-driven writes. <br>
Mitigation: Install it with a tightly scoped management account, preferably read-only until writes are intentionally needed; use dry-run and confirmation paths before profile assignment or reboot. <br>
Risk: Endpoint credentials and local audit or undo data may expose sensitive endpoint, user, profile, or management-server information. <br>
Mitigation: Treat ENDPOINT_AIOPS_MASTER_PASSWORD as a secret, avoid long-lived shell exports where possible, and review local ~/.endpoint-aiops data handling for sensitive environments. <br>
Risk: The REST paths and some dialect behavior are modelled and have not been exercised against a live endpoint-management server. <br>
Mitigation: Run endpoint-aiops doctor and validate behavior against a non-production or read-only target before relying on results or enabling write operations. <br>


## Reference(s): <br>
- [Endpoint Aiops ClawHub page](https://clawhub.ai/zw008/skills/endpoint-aiops) <br>
- [Endpoint-AIops project homepage](https://github.com/AIops-tools/Endpoint-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and structured tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool results may include capped list envelopes with returned, limit, and truncated fields; write workflows may record audit and undo state locally.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
