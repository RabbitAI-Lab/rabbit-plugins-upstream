## Description:

GitHub Flow helps agents manage GitHub issues, pull requests, reviews, merge checks, publishing steps, and repository hygiene workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to turn implementation plans and repository changes into GitHub issues, PRs, reviews, test plans, and guarded merge workflows. It is intended for GitHub-backed repositories where the agent is expected to operate through the gh CLI and maintain explicit checks before publishing or merging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through live GitHub repository changes, including issue and PR edits, comments, readiness changes, merges, token scope refreshes, and GitHub account switching.

Mitigation: Install only when those capabilities are desired, review account mappings and scope-refresh rules before use, and require explicit confirmation for publish, comment, reviewer, dependency, push, ready, and merge actions.

Risk: Repository publication workflows can expose unintended content in public issues, PR bodies, comments, or review text.

Mitigation: Apply the skill's public-repository sanitize checks before posting externally visible content, and review generated text before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Publisher profile](https://clawhub.ai/user/drumrobot)
- [GitHub Flow overview](SKILL.md)
- [PR creation guide](pr.md)
- [Merge guide](merge.md)
- [Sanitize guide](sanitize.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and GitHub CLI procedures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include issue bodies, PR bodies, review comments, merge checklists, branch and publishing commands, and repository policy guidance.]

## Skill Version(s):

0.10.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
