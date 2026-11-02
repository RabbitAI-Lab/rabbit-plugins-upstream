## Description:

Pair-style code quality reviewer: twelve book-grounded decay risks (R1–R6, T1–T6) plus release-safety and first-paint UX checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review code, pull requests, architecture, and tests for maintainability, release-safety, and first-paint usability risks. It produces evidence-based findings and a per-review health deduction index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading the skill may overwrite local skill files or customizations.

Mitigation: Preview installation targets with --dry-run and back up local skill customizations before upgrading.

Risk: An npm release may differ from the reviewed version.

Mitigation: Pin npm installation to the reviewed version, 0.4.4.

Risk: Optional hooks may behave differently across agent hosts.

Mitigation: Test optional hooks with the intended host before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-code-quality)
- [Project homepage](https://github.com/YottaMeta/yotta-code-quality)
- [Code review workflow and scoring](references/common.md)
- [Production decay risks](references/decay-risks.md)
- [Test quality risks](references/test-decay-risks.md)
- [Release safety and first-paint checks](references/editorial-extensions.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review report with structured findings and a per-review health deduction index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports in the user's language; read-only by default. Code changes require an explicit request or --fix.]

## Skill Version(s):

0.4.4 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
