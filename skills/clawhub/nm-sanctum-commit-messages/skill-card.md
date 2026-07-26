## Description: <br>
Generates conventional commit messages from staged changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect staged Git changes and draft a human-readable Conventional Commit message before committing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Staged Git diffs may contain secrets or sensitive business context that the agent will read while drafting the message. <br>
Mitigation: Review staged changes before invoking the skill and use it only in repositories where the agent is allowed to inspect the staged diff. <br>
Risk: The workflow writes commit_msg.txt in the current directory. <br>
Mitigation: Check for an existing commit_msg.txt before use if that filename may already contain user-managed content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-commit-messages) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown commit message text written to commit_msg.txt with a preview.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads staged Git context and produces a proposed commit subject, optional body, and optional footer.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
