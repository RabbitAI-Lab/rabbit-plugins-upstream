## Description: <br>
Manage Git commits, branches, merges, and versioning with structured workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to plan disciplined Git workflows, create atomic commits, manage short-lived branches and worktrees, and prepare semantic version releases with changelogs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest destructive Git operations such as resetting work, removing worktrees, creating tags, or pushing tags. <br>
Mitigation: Review proposed Git commands before execution, confirm the current branch and working tree state, and avoid destructive or publishing operations unless the repository state and release intent are clear. <br>
Risk: The artifact is a guidance-only skill and its command examples should not be treated as automatic actions. <br>
Mitigation: Use the examples as prompts for human-reviewed workflow decisions and run project-specific tests, linting, and secret checks before committing or releasing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/git-workflow-and-versioning) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Git and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language workflow guidance; no executable payload is included in the release artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
