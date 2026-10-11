## Description:

Guides an AI coding assistant through iterative code review, fixes, validation, and defensive implementation of coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to review and improve a codebase in multiple rounds, or to make incremental code changes with validation after each step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured validation or invariant commands may execute untrusted repository code under the user's account.

Mitigation: Install only in trusted repositories and review validation.commands and invariants.commands before running checks.

Risk: Automatic fixes can modify code beyond the intended change.

Mitigation: Use review-only mode for untrusted projects and review proposed changes before accepting them.

Risk: Enabling automatic merge or per-round push can publish changes without a final manual review.

Mitigation: Leave auto_merge and push_per_round disabled unless automated publishing is intentional.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Code changes and Markdown review summaries with validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only mode can report findings without changing code.]

## Skill Version(s):

3.4.4 (source: SKILL.md frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
