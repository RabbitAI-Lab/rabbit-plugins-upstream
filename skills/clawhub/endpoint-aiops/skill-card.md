## Description: <br>
Provides governed managed-endpoint fleet operations for health overview, inventory, endpoint scoring, login-storm analysis, drift and patch checks, profile assignment, and reboot workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, IT operators, and endpoint administrators use this skill to inspect managed endpoint fleets, diagnose login storms and drift, assess patch compliance, and perform guarded remediation actions such as assigning profiles or rebooting endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform disruptive endpoint changes, including profile assignment and reboots, without its own read-only or approval gate. <br>
Mitigation: Use a read-only management account by default, grant write-capable credentials only when endpoint changes are approved, and use dry-run previews before state-changing operations. <br>
Risk: A broadly inherited master-password environment variable can expose access to the encrypted credential store. <br>
Mitigation: Provide ENDPOINT_AIOPS_MASTER_PASSWORD only to the intended MCP or CLI process, or use an interactive prompt for local CLI sessions. <br>
Risk: Legacy plaintext API-key environment variables may still be honored as fallback credentials. <br>
Mitigation: Migrate legacy API-key variables into the encrypted secret store and remove them from shell profiles, CI settings, and shared environments. <br>
Risk: Modeled endpoint-management REST paths have not been exercised against a live management server. <br>
Mitigation: Run endpoint-aiops doctor and validate read operations in a non-production or read-only environment before enabling write-capable credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/endpoint-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Endpoint-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes capped-list truncation indicators, uncapped fleet totals, risk-tier labels for write actions, and dry-run guidance for state-changing commands.] <br>

## Skill Version(s): <br>
0.8.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
