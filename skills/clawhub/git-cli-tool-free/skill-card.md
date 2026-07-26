## Description: <br>
Git命令行助手免费版 helps developers use Git CLI workflows by providing command references, repository status checks, staging and commit guidance, branch management, and remote synchronization guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill for day-to-day Git command-line support, including quick command lookup, repository diagnosis, staging and committing changes, branch management, and remote synchronization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through write-enabled Git operations and remote synchronization workflows. <br>
Mitigation: Require the agent to show git status and git diff, list exact files to stage, confirm the commit message, and confirm the branch and remote URL before write actions. <br>
Risk: Credential storage and force-style pushes can create avoidable repository or account risk. <br>
Mitigation: Avoid global credential storage and force-style pushes unless the user explicitly confirms the intent and scope. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/git-cli-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Git commands, shell snippets, JSON examples, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include repository checks, exact Git commands, commit guidance, branch and remote synchronization steps, and safety reminders.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
