## Description: <br>
Generates conventional commit messages from staged changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to inspect staged Git changes and draft a concise conventional commit message with an appropriate type, optional scope, body, and footer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Git-related triggers may activate the skill during general Git conversations. <br>
Mitigation: Confirm the intended repository and staged changes before asking the agent to draft a commit message. <br>
Risk: The workflow writes a local ./commit_msg.txt draft file. <br>
Mitigation: Run it only in the intended working tree and review, rename, or remove the generated draft file as needed. <br>
Risk: Generated commit text may omit or mischaracterize staged changes. <br>
Mitigation: Compare the draft against git status and the staged diff before using it for a commit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-commit-messages) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, files] <br>
**Output Format:** [Markdown/plain text conventional commit message with a local commit_msg.txt draft file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafts from staged Git state; does not execute commits or bypass hooks.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
