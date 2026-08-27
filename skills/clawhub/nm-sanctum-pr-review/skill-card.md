## Description:

Reviews pull requests with scope validation, requirements compliance, and line comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review GitHub or GitLab pull and merge requests against stated scope, requirements, version consistency, and review hygiene before merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review details may be posted publicly or persisted through PR comments, issues, reports, Discussions, or knowledge capture.

Mitigation: Review findings before publishing, avoid including secrets or sensitive security details in public comments, and disable or explicitly confirm knowledge capture when needed.

Risk: Broad review-related triggers could invoke the skill when the user only intended a lighter review workflow.

Mitigation: Prefer explicit invocation and confirm the target PR or MR before allowing comment, issue, report, or knowledge-capture actions.

Risk: Backlog issue creation and review posting can change repository state.

Mitigation: Require user confirmation before creating issues or submitting review comments, and use local report output when a non-mutating review is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-pr-review)
- [ClawDIS homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown reports with inline comments, review summaries, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or post PR comments, create backlog issues after confirmation, write local reports, and capture review knowledge depending on the execution environment and user approval.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
