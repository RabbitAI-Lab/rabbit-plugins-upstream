## Description:

GitHub CLI for issues, PRs, CI/check logs, comments, reviews, releases, repos, and gh api queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to operate GitHub repositories through the GitHub CLI for pull requests, issues, CI runs, reviews, releases, repository queries, and direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitHub CLI commands can change repositories by merging pull requests, creating or closing issues, posting comments, or rerunning workflows.

Mitigation: Require clear confirmation before repository-changing commands and verify the target repository and GitHub account first.

Risk: A mismatched GitHub CLI authentication directory can cause commands to run under an unexpected account.

Mitigation: Check gh auth status and configure GH_CONFIG_DIR deliberately when the gateway environment differs from the operator environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/github)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and GitHub CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gh --json, --jq, and --body-file usage for structured output and safer multi-line request bodies.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
