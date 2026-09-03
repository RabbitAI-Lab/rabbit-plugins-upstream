## Description:

Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting an AI Review Summary and Formal Review, and registering deferred items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering reviewers use this skill to consolidate CodeRabbit, GitHub Copilot, human, and internal review feedback on pull requests or issues, decide how findings should be handled, and publish a clear review summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish GitHub comments or Formal Reviews and may do so with limited confirmation in non-interactive paths.

Mitigation: Prefer running with --interactive and review drafted summaries or review bodies before allowing them to be posted.

Risk: The workflow can mutate review tracking state, including local checklist-style files or GitHub issues for deferred findings.

Mitigation: Run it only in repositories where this automation is acceptable, and inspect proposed tracking changes before committing or publishing them.

Risk: GitHub account and token scope affect what the skill can read, publish, edit, or submit as a review.

Mitigation: Use the least-privileged GitHub account and token suitable for the target repository and confirm the active account before posting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill workflow](SKILL.md)
- [PR workflow topic](pr.md)
- [Posting workflow topic](post.md)
- [Superpowers plugin](https://github.com/obra/superpowers)
- [receiving-code-review](https://skills.sh/obra/superpowers/receiving-code-review)
- [requesting-code-review](https://skills.sh/obra/superpowers/requesting-code-review)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown review summaries, Formal Review bodies, shell commands, and optional tracking-file edits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish GitHub review comments and update local tracking files when the workflow proceeds.]

## Skill Version(s):

0.6.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
