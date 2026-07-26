## Description: <br>
Git-based version control for OpenClaw system configuration changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to create Git checkpoints before sensitive configuration changes and roll back to earlier configuration states when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hard rollback can discard uncommitted OpenClaw configuration changes. <br>
Mitigation: Review git status and git diff before rollback, show the user what will be discarded, and confirm the target commit before running git reset --hard. <br>
Risk: Sensitive credentials or session logs could be captured if ignore rules are incomplete. <br>
Mitigation: Confirm .gitignore excludes credentials, session logs, databases, temporary files, and other volatile or sensitive paths before saving checkpoints. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/evezart/git-version-control) <br>
- [Publisher profile](https://clawhub.ai/user/evezart) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes checkpoint, rollback, status, history, diff, and .gitignore guidance for OpenClaw configuration repositories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
