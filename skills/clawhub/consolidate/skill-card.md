## Description:

Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting an AI Review Summary and Formal Review, and registering deferred items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to review pull request or issue feedback from tools such as CodeRabbit and GitHub Copilot, classify findings, decide whether to fix or defer them, and publish a consolidated review summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish GitHub reviews, block merges, edit PR metadata, and persist follow-up tasks using the invoking user's authenticated account.

Mitigation: Use explicit invocation, enable interactive mode for every run, use a narrowly scoped GitHub token, and review PR-body edits, formal review events, inline comments, and deferred tracking writes before they are sent or saved.

Risk: Packaged hooks can affect review or merge workflows if registered broadly.

Mitigation: Avoid registering the packaged hooks globally; scope hook use to repositories and sessions where this review automation is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill workflow topics](SKILL.md)
- [superpowers dependency](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with review summaries, formal review text, optional inline review comments, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create PR comments, formal review events, PR-body edits, and deferred tracking entries when invoked with authenticated GitHub access.]

## Skill Version(s):

0.6.3 (source: frontmatter, changelog released 2026-09-05, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
