## Description: <br>
Automatically updates a repository's PROJECT_STATE.md after each commit with recent Git context and optional AI-generated summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joe3112](https://clawhub.ai/user/joe3112) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users install this skill in a Git repository to keep a local project-state file current across commits, making future agent sessions easier to resume. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs a persistent Git post-commit hook that updates repository files after commits. <br>
Mitigation: Install it only in repositories where automatic PROJECT_STATE.md updates are expected, and use the uninstall script or inspect .git/hooks/post-commit to remove it. <br>
Risk: AI summary mode may send commit messages, filenames, branch state, and related repository metadata to the configured local Clawdbot gateway. <br>
Mitigation: Enable AI summaries only when the gateway configuration, authentication, logging, and any downstream model routing are acceptable for the repository's data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/joe3112/skills/project-context-sync) <br>
- [Clawdbot gateway](https://github.com/clawdbot/clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance] <br>
**Output Format:** [Markdown files, YAML configuration, and shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates PROJECT_STATE.md, .project-context.yml, .gitignore, and a Git post-commit hook in the target repository.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
