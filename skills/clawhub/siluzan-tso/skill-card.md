## Description: <br>
Siluzan TSO routes advertising, account-management, finance, analytics, reporting, and market-analysis tasks through the Siluzan TSO CLI and its supporting workflow references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External advertising operators and analysts use this skill to route Siluzan TSO work across paid-media accounts, campaign setup and changes, financial/account operations, performance reporting, website diagnosis, keyword planning, and market analysis. It is intended for environments where the user has authorized access to the relevant advertising accounts and business data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: One-click installation may change npm configuration, install global tooling, register the skill across multiple assistants, and store Siluzan credentials. <br>
Mitigation: Review installer effects before running it, prefer an isolated or managed environment, and confirm where credentials and assistant registrations will be stored. <br>
Risk: Authenticated workflows can affect real advertising accounts, campaigns, reports, finance/account operations, and account-opening processes. <br>
Mitigation: Use only with authorized accounts, verify the target account and submitted data, and require explicit user confirmation before write, delete, publish, or commit-style actions. <br>
Risk: Stored Siluzan credentials can provide persistent access after setup. <br>
Mitigation: Limit installation to trusted machines, avoid shared environments, and rotate or revoke credentials when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso) <br>
- [Skill Routing Table](artifact/SKILL.md) <br>
- [Documentation Directory](artifact/AGENTS.md) <br>
- [Setup and Authentication](artifact/references/core/setup.md) <br>
- [Agent Conventions](artifact/references/core/agent-conventions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON-backed reports, HTML or Excel report files, and shell command sequences] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses siluzan-tso CLI workflows; many data workflows write JSON output before producing human-facing reports.] <br>

## Skill Version(s): <br>
1.1.39 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
