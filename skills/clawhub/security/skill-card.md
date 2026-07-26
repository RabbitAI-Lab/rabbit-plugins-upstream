## Description: <br>
AgentGuard helps agents audit installed skills, credentials, permissions, network exposure, runtime actions, and OpenClaw patrols, then returns security reports and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xbeekeeper](https://clawhub.ai/user/0xbeekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use AgentGuard to scan skills and code, evaluate proposed runtime actions, manage skill trust records, run OpenClaw security patrols, and generate agent health reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad local visibility into installed skills, workspaces, credential-directory metadata, environment names, agent configs, network state, cron jobs, and Web3 action context. <br>
Mitigation: Install only when this security-auditor access is intended, and review generated reports before sharing them. <br>
Risk: Ongoing local monitoring through auto-scan or daily patrol can collect repeated security posture details. <br>
Mitigation: Enable auto-scan or daily patrol only when continuous monitoring is desired, and periodically review the configured hooks, cron entries, and audit log. <br>
Risk: The security summary notes fail-open or under-scoped behavior. <br>
Mitigation: Verify the AgentGuard dependency and version before use, and manually review high-risk findings before relying on allow, deny, or confirm recommendations. <br>


## Reference(s): <br>
- [ClawHub AgentGuard skill page](https://clawhub.ai/0xbeekeeper/skills/security) <br>
- [README.md](README.md) <br>
- [scan-rules.md](scan-rules.md) <br>
- [action-policies.md](action-policies.md) <br>
- [patrol-checks.md](patrol-checks.md) <br>
- [web3-patterns.md](web3-patterns.md) <br>
- [evals.md](evals.md) <br>
- [GoPlus Security](https://gopluslabs.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, JSON action decisions, generated HTML health reports, and configuration or audit files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+. Optional GoPlus API credentials enable enhanced Web3 transaction simulation.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
