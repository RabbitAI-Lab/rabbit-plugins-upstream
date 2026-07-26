## Description: <br>
Analyze agent run logs for errors, token spikes, and failures with JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Agent Logger to scan local agent run logs for errors, warnings, token spikes, and health status, then feed JSON reports into dashboards or CI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Log samples can include sensitive operational details when reports are shared outside the local workspace. <br>
Mitigation: Review and redact scanned logs or generated error samples before sharing outputs. <br>
Risk: Included CI scripts execute local verification checks when invoked. <br>
Mitigation: Review the scripts and run them only in a trusted local or CI environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/agent-logger) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>
- [Artifact README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON reports, with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline Python CLI using the standard library; scans local .log, .txt, and .json files and includes up to five error samples.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
