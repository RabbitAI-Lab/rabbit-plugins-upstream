## Description: <br>
Comprehensive security audit for OpenClaw that scans 7 domains (runtime, channels, agents, cron, skills, sessions, network), supports 3 expertise levels, context-aware analysis, and visual dashboard, and produces read-only localized reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jooneyp](https://clawhub.ai/user/jooneyp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw operators use Secucheck to audit local OpenClaw configuration, runtime exposure, agent permissions, cron jobs, installed skills, sessions, and network posture, then review findings and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs active shell-based local inspection across OpenClaw configuration, runtime, network, permissions, agent, workspace, and skill state. <br>
Mitigation: Install and run it only when an active OpenClaw security audit is intended, and avoid running it with sudo or root privileges. <br>
Risk: The skill can auto-run reviews and serve a generated security dashboard, which may expose host and agent details if reachable beyond the local machine. <br>
Mitigation: Review or disable auto-review and dashboard behavior before use, prefer localhost-only serving, and do not publish generated dashboard URLs broadly. <br>
Risk: Generated reports can include sensitive host, network, permissions, workspace, and agent information. <br>
Mitigation: Treat reports and dashboard files as sensitive operational data, restrict access, and remove them when no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jooneyp/skills/secucheck) <br>
- [README](artifact/README.md) <br>
- [Runtime Security Checks](artifact/checks/runtime.md) <br>
- [Network Security Checks](artifact/checks/network.md) <br>
- [Agent Security Checks](artifact/checks/agents.md) <br>
- [Prompt Injection Scenario](artifact/scenarios/prompt-injection.md) <br>
- [Unauthorized Access Scenario](artifact/scenarios/unauthorized-access.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown reports, JSON audit data, shell-command recommendations, and generated HTML dashboard files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Localized report language and expertise-level detail can vary by user selection.] <br>

## Skill Version(s): <br>
2.8.0 (source: server release metadata and artifact/skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
