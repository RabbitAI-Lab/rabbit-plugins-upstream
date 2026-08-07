## Description:

GitHub Flow helps agents convert plans, research, reviews, and implementation work into GitHub issues, pull requests, review comments, dependency updates, publishing flows, sanitization checks, and merges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to manage GitHub issue and pull request workflows with test plans, review comments, dependency relationships, publish and merge gates, and pre-publication sanitization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through broad GitHub workflow actions, including issue creation, dependency mutations, reviewer registration, pushes, pull request state changes, and merges.

Mitigation: Use a dedicated, least-privilege GitHub account or token and require explicit user confirmation before each write or merge action.

Risk: Account or token confusion could cause actions to run under the wrong GitHub identity.

Mitigation: Verify repository ownership and active account before committing, pushing, reviewing, or merging; prefer command-scoped token use when account switching is unreliable.

Risk: Issue, pull request, commit, or review text could expose personal data, private repository references, local paths, or internal-only details.

Mitigation: Run the documented visibility check and sanitization scans before posting or editing public-facing GitHub content.

Risk: Automated workflow guidance can make state changes that are hard to unwind, such as dependency relationships, ready-for-review transitions, and merge operations.

Mitigation: Review the generated plan, test plan status, dependency state, and CI/review gates before applying the proposed command sequence.

## Reference(s):

- [GitHub Flow skill overview](artifact/SKILL.md)
- [Authentication and scope guidance](artifact/auth-scope.md)
- [Pull request workflow guidance](artifact/pr.md)
- [Merge workflow guidance](artifact/merge.md)
- [Sanitization guidance](artifact/sanitize.md)
- [Issue dependency guidance](artifact/dependencies.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and occasional script or JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce issue bodies, pull request bodies, review comments, merge plans, GitHub CLI commands, GraphQL snippets, and local validation commands.]

## Skill Version(s):

0.8.1 (source: server release metadata and changelog, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
