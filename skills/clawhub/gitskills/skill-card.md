## Description: <br>
Manages GitHub repositories, branches, pull requests, and issues through the GitHub API; it is not for repository cloning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage GitHub repository lifecycle tasks, branches, pull requests, and issues from agent-guided commands backed by the GitHub API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a GitHub token with repository, pull request, and issue permissions. <br>
Mitigation: Use a fine-scoped token and grant delete or write privileges only when the intended workflow needs them. <br>
Risk: Repository deletion is irreversible and is available through the skill. <br>
Mitigation: Review the target repository carefully, keep backups where appropriate, and confirm destructive commands only after checking the requested action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/gitskills) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Text and Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a GitHub API token supplied through GITHUB_TOKEN.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter, _meta.json, server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
