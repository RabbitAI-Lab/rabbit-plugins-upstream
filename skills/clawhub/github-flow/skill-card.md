## Description:

GitHub issue and pull request workflow automation for planning issues, creating PRs, managing dependencies, reviewing changes, publishing branches, applying feedback, sanitizing public content, and merging with checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to turn plans and implementation work into GitHub issues, PRs, reviews, dependency links, and guarded merge workflows. It is intended for repositories where the team's process matches its GitHub CLI, account-mapping, sanitization, review, and merge conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use broad GitHub CLI credentials and perform durable repository actions such as creating or editing issues, PRs, reviews, merges, and dependency relationships.

Mitigation: Install it only for repositories where those actions are intended, review the configured GitHub account and scopes before use, and keep user approval gates for branch changes, pushes, ready transitions, and merges.

Risk: The skill includes account switching and GH_TOKEN fallback patterns, which can act with a different GitHub identity than expected if the environment is misconfigured.

Mitigation: Verify the active GitHub account, repository owner mapping, and token scope before committing, pushing, creating PRs, or merging.

Risk: The workflow can publish generated issue, PR, review, and merge text to public repositories.

Mitigation: Run the documented sanitization checks for public content, internal paths, private repository references, and language rules before posting.

Risk: The skill persists and consumes local workflow state, including deferred review-feedback tracking.

Mitigation: Review local state before applying deferred feedback, and verify that target PRs, files, and findings are still current before editing or pushing changes.

## Reference(s):

- [GitHub Flow skill overview](SKILL.md)
- [Authentication and scope guidance](auth-scope.md)
- [Pull request workflow](pr.md)
- [Merge workflow](merge.md)
- [Sanitization guidance](sanitize.md)
- [Release changelog](CHANGELOG.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with GitHub CLI commands, checklists, templates, and workflow rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce issue bodies, PR bodies, review comments, merge instructions, dependency updates, and local workflow-state updates through an agent.]

## Skill Version(s):

0.11.1 (source: release evidence and changelog, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
