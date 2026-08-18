## Description:

GitHub Flow helps agents manage GitHub issue and pull request workflows, including issue drafting, PR creation, review posting, merge gates, auth handling, dependency tracking, push safeguards, and public-repository sanitization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and repository maintainers use this skill to turn plans and implementation results into GitHub issues and pull requests, coordinate review and merge workflows, and apply safeguards before publishing public repository content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad GitHub repository operations, including authentication scope changes, PR creation, comments, review posting, merges, and local git cleanup.

Mitigation: Require explicit confirmation for every remote write, review the target repository and account before execution, and avoid broad gh auth scope refreshes unless they are necessary.

Risk: The security summary reports broad repository and credential authority with several under-scoped or contradictory safety gates.

Mitigation: Treat gate checks as mandatory review points, verify CI and review evidence before merge actions, and pause when a gate or instruction conflicts.

Risk: GH_TOKEN and private repository context can expose sensitive data if reused or published carelessly.

Mitigation: Treat GH_TOKEN as sensitive, keep tokens out of generated text, and do not rely on private-repo exceptions for secrets or internal infrastructure data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Publisher profile](https://clawhub.ai/user/drumrobot)
- [Skill manifest](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)
- [License](artifact/LICENSE)
- [Identity and auth guide](artifact/identity-auth.md)
- [Pull request guide](artifact/pr.md)
- [Merge guide](artifact/merge.md)
- [Push guards guide](artifact/push-guards.md)
- [Public repository sanitization guide](artifact/sanitize.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and small script or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output is intended for GitHub repositories and gh CLI workflows; remote writes should be explicitly confirmed before execution.]

## Skill Version(s):

0.8.3 (source: ClawHub release evidence and CHANGELOG.md, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
