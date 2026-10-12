## Description:

Consolidates external feedback on pull requests and issues into classified findings, review decisions, and published review summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to collect AI and internal code reviews, assess findings against a pull request, decide on fixes, and publish review summaries and formal reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review automation can publish or change PR comments and formal reviews using a GitHub token.

Mitigation: Use a trusted GitHub account with limited token permissions and enable interactive review before posting.

Risk: Reviewing external-contributor branches may run untrusted tests or builds.

Mitigation: Disable local test and build execution or run it in a sandbox before reviewing untrusted branches.

Risk: Plugin or hook installation can alter the local development environment.

Mitigation: Review the installation behavior and install only in a trusted development environment.

## Reference(s):

- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [Superpowers code-review skills](https://github.com/obra/superpowers)
- [Receiving Code Review](https://skills.sh/obra/superpowers/receiving-code-review)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown review findings, PR summaries, and formal reviews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish or update GitHub PR comments and formal reviews.]

## Skill Version(s):

0.8.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
