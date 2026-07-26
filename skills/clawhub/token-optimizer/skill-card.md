## Description: <br>
Tokenoptimizer helps OpenClaw users reduce AI API spend by applying lower-cost model routing, local or disabled heartbeat options, prompt caching, lean session templates, and budget controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smartpeopleconnected](https://clawhub.ai/user/smartpeopleconnected) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to analyze token usage, preview and apply cost-focused OpenClaw configuration changes, generate prompt and session templates, and verify the resulting setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Applied optimization changes can alter OpenClaw model routing, heartbeat, budget, workspace, prompt, and stats files under ~/.openclaw/. <br>
Mitigation: Review dry-run output and generated files before running with --apply, and use generated backups or rollback commands when config restoration is needed. <br>
Risk: Provider reachability checks may contact local or configured endpoints and create outbound network logs. <br>
Mitigation: Avoid or constrain provider reachability checks where network logging, privacy, or policy requirements are a concern. <br>
Risk: Broad cost-optimization triggers could invoke the skill in contexts where configuration changes are not intended. <br>
Mitigation: Narrow or disable broad triggers in environments that support trigger configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smartpeopleconnected/skills/token-optimizer) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Project Homepage](https://github.com/smartpeopleconnected/openclaw-token-optimizer) <br>
- [Project Issues](https://github.com/smartpeopleconnected/openclaw-token-optimizer/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON configuration, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Dry-run previews are the default; applying changes can write OpenClaw configuration, workspace templates, prompt rules, backups, and usage stats under ~/.openclaw/.] <br>

## Skill Version(s): <br>
1.0.18 (source: server release metadata, artifact metadata, skill.json, src/__init__.py, CHANGELOG released 2026-02-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
