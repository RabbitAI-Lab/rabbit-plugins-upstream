## Description:

GitHub helps agents use the gh CLI to query issues, read issue content and screenshots, publish branches, and create pull requests with configured defaults.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to inspect GitHub-tracked work, handle issue screenshots honestly, and prepare or verify pull requests using local configuration and the GitHub CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use the user's GitHub CLI login to read private issue content and create or auto-merge pull requests when requested or configured.

Mitigation: Before use, review .claude/github.json and ~/.claude/github.json defaults, especially autoMerge, linkKeyword, targetBranch, and reviewers; use a GitHub CLI account whose repository access matches the intended work.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose GitHub CLI commands, issue summaries, screenshot status reports, pull request descriptions, and configuration defaults for review before action.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
