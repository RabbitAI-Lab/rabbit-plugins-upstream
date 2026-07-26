## Description: <br>
Diagnose and fix cron job issues: missed runs, overlapping jobs, silent failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and SREs use Cron Doctor to validate crontab-style scheduled-task files, flag unsafe commands, and catch parse or overlap issues before scheduled jobs run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional CI verification helper can run Python tests when explicitly used on a target folder. <br>
Mitigation: Run CI helpers only against trusted or isolated repositories without access to secrets or sensitive filesystem paths. <br>
Risk: Cron diagnostics can flag unsafe commands but do not make scheduled commands safe to execute. <br>
Mitigation: Review reported commands manually before deploying or modifying scheduled jobs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/cron-doctor) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/itspremkumar) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text summaries or JSON diagnostics, with documented shell commands for local and CI use.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stdlib Python 3.8+; offline local file checker with optional non-zero CI failure behavior.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
