## Description:

Work with GitHub issues and pull requests via the gh CLI by querying assigned or milestone issues, reading issue descriptions and embedded screenshots, publishing branches, and creating PRs with configured reviewer, auto-merge, branch, title, and issue-linking defaults.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to manage GitHub-tracked work through the gh CLI, including assigned issue lookup, issue reading with screenshot handling, and pull request creation with configured repository defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub tokens can be exposed through local process arguments when downloading private repository attachments with a curl Authorization header populated from gh auth token.

Mitigation: Review the skill before use with private repositories or write-capable GitHub credentials, prefer a token-passing method that avoids process arguments, and confirm PR creation, issue-closing keywords, reviewers, and auto-merge settings before repository-changing actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose gh CLI commands, summarize GitHub issue and PR state, and offer to create .claude/github.json configuration when missing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
