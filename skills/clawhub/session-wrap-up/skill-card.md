## Description: <br>
Wrap up a conversation session by saving context to memory files, updating PARA notes, committing changes, and summarizing the session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[branexp](https://clawhub.ai/user/branexp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill at the end of a work session to preserve decisions, update memory and PARA notes, commit repository changes, and report follow-up items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically stages, commits, and pushes session-derived files to the configured Git remote without a review step. <br>
Mitigation: Use it in a dedicated repository, keep secrets and private files out of scope, verify `.gitignore`, and manually review changed files and the remote destination before pushing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/branexp/skills/session-wrap-up) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown text with shell commands and repository file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stage, commit, and push repository changes when followed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
