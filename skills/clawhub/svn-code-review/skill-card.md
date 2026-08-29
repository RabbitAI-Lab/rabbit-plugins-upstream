## Description:

Helps agents request SVN-based code reviews after completing tasks, major features, or pre-merge checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouzy-creator](https://clawhub.ai/user/zhouzy-creator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to trigger a structured code review for SVN revision ranges, compare implementation work against requirements, and classify production-readiness issues by severity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected code changes and requirements may be shared with a reviewer subagent during use.

Mitigation: Review the material being sent and avoid including unrelated or sensitive changes in the review context.

Risk: An incorrect SVN revision range can include unrelated changes or omit relevant work.

Mitigation: Confirm the base and head revisions before dispatching the review workflow.

## Reference(s):

- [Source repository](https://github.com/zhouzy-creator/svn_code_review)
- [ClawHub skill page](https://clawhub.ai/zhouzy-creator/skills/svn-code-review)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Analysis]

**Output Format:** [Markdown review instructions and categorized review findings with inline SVN commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit base and head SVN revisions to limit the reviewed change set.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
