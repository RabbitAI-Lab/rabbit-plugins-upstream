## Description: <br>
Track and analyze Monkeytype typing statistics with improvement tips, including on-demand stats, test history analysis, personal bests, progress comparison, leaderboard lookup, and optional automated reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qrucio](https://clawhub.ai/user/qrucio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to connect a Monkeytype ApeKey, retrieve typing statistics, compare recent progress, inspect leaderboard results, and receive targeted typing improvement tips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Monkeytype ApeKey, which could be exposed if pasted into chat or stored in plaintext. <br>
Mitigation: Prefer MONKEYTYPE_APE_KEY and rotate or delete the local config if the skill is uninstalled or the machine is no longer trusted. <br>
Risk: Optional daily or weekly reports create recurring local jobs. <br>
Mitigation: Enable scheduled reports only when wanted and review the saved automation settings during setup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/qrucio/skills/monkeytype-tracker) <br>
- [Monkeytype API Base URL](https://api.monkeytype.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and plain-text statistics from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a local Monkeytype config file and optional scheduled report settings when the user enables automation.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
