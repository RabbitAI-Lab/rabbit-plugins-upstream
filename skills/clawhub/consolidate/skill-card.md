## Description:

Consolidate helps an agent gather PR or issue review feedback, classify findings, produce review summaries, and post formal GitHub review artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to consolidate CodeRabbit, GitHub Copilot, human, and internal review feedback on pull requests or issues. It helps produce structured AI Review Summary and Formal Review outputs while preserving user decisions for posting and follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on untrusted PR code and local repositories.

Mitigation: Run review and verification steps for untrusted forks or PRs in a disposable sandbox without home-directory credentials, broad tokens, SSH keys, or cloud credentials mounted.

Risk: The skill can post or patch GitHub reviews and comments.

Mitigation: Use least-privilege GitHub credentials and keep interactive review enabled when publication decisions or review text require human approval.

Risk: Autonomous review sessions and generated summaries can publish incorrect or misleading claims.

Mitigation: Review generated review bodies before posting and use the included validation or hook scripts only after checking the blocking rules they enforce.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill definition](SKILL.md)
- [PR workflow guide](pr.md)
- [Collect AI reviews guide](collect.md)
- [Analyze and classify guide](classify.md)
- [Internal review fallback guide](internal.md)
- [Post summary and formal review guide](post.md)
- [Next-action guide](next.md)
- [Superpowers plugin](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown review summaries, formal review text, inline review comments, and shell or GitHub CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create draft files and post or patch GitHub PR reviews or issue comments when approved by the workflow.]

## Skill Version(s):

0.6.5 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
