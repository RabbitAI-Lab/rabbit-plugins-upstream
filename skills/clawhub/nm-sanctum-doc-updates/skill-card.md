## Description:

Updates documentation after code changes with quality gates, slop detection, and accuracy checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill after code changes to identify documentation targets, update user-facing docs and docstrings, check consolidation opportunities, and verify documentation accuracy before review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation consolidation can remove or merge useful content if accepted without review.

Mitigation: Review every proposed deletion or merge, and use the dry-run or skip options when uncertain.

Risk: Documentation updates can introduce stale version numbers, broken paths, or inaccurate counts.

Mitigation: Run the skill's accuracy checks against the current codebase and review warnings before finalizing changes.

Risk: Broad triggers may route unrelated writing tasks into a repository documentation workflow.

Mitigation: Use the skill for documentation work tied to code changes and avoid broad triggers for unrelated writing requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-doc-updates)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces documentation edits, review checklists, consolidation proposals, and validation commands.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
