## Description: <br>
Classify every shell command as SAFE, WARN, or CRIT before your agent runs it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[globalcaos](https://clawhub.ai/user/globalcaos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add pre-execution shell command classification, logging, and approval gates for OpenClaw or TinkerClaw-style agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included installer scripts can modify and rebuild an OpenClaw codebase, which is high-impact behavior for a command-classification skill. <br>
Mitigation: Review the scripts and exact source changes before running them, use only a trusted expected OpenClaw checkout, and keep a clean backup or version-control rollback available. <br>
Risk: The rebuild step executes code from the target checkout. <br>
Mitigation: Treat rebuild commands as code execution from that checkout and run them only in an environment where that code and dependencies are trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/shell-security-ultimate) <br>
- [TinkerClaw project](https://github.com/globalcaos/clawdbot-moltbot-openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with shell commands, Python helper output, and patch scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SAFE, WARN, and CRIT command labels; included patch scripts modify and rebuild a local OpenClaw checkout when run.] <br>

## Skill Version(s): <br>
2.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
