## Description:

GoPlus AgentGuard is an AI agent security guard for scanning skills and code, evaluating action safety, managing trust, running security patrols, and generating health-check reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xbeekeeper](https://clawhub.ai/user/0xbeekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and security reviewers use AgentGuard to inspect installed skills and codebases, evaluate proposed runtime actions, maintain skill trust records, run OpenClaw patrol checks, and produce security health-check reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs broad local inspection of agent directories, workspace contents, environment-variable names, cron entries, and network state.

Mitigation: Install and run it only in environments where that inspection is acceptable, and review the configured filesystem access paths before use.

Risk: Generated HTML reports can load remote code and may open automatically.

Mitigation: Open reports only from trusted runs, review report files before sharing, and prefer dedicated or isolated environments for checkups.

Risk: Web3 transaction simulation is enhanced by optional GoPlus credentials and otherwise falls back to policy-based checks.

Mitigation: Configure GOPLUS_API_KEY and GOPLUS_API_SECRET for Web3 simulation when needed, and treat fallback results as less complete.

## Reference(s):

- [AgentGuard ClawHub release](https://clawhub.ai/0xbeekeeper/skills/security)
- [README](README.md)
- [Scan Rules](scan-rules.md)
- [Action Policies](action-policies.md)
- [Patrol Checks](patrol-checks.md)
- [Web3 Patterns](web3-patterns.md)
- [Evaluation Scenarios](evals.md)
- [GoPlus Security API documentation](https://docs.gopluslabs.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, JSON decisions, shell commands, configuration updates, and generated HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write audit and configuration files under ~/.agentguard and generate browser-viewable HTML checkup reports.]

## Skill Version(s):

1.0.12 (source: ClawHub server release evidence; artifact metadata version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
