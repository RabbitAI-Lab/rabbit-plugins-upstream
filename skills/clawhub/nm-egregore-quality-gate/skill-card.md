## Description:

Orchestrates the QUALITY pipeline stage for egregore work items, running code review, unbloat, and test updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to run egregore quality-stage checks, self-review branches, update tests or documentation, and review pull requests before merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically commit changes or post GitHub pull-request approvals, comments, or change requests.

Mitigation: Use explicit invocation, verify the target branch and pull-request number before running, and add confirmation or dry-run controls before use in shared repositories.

Risk: Broad triggers such as "quality" and "review" may invoke the skill in contexts where its egregore-specific workflow is not intended.

Mitigation: Narrow trigger configuration or reserve the skill for egregore quality-stage work items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-quality-gate)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/egregore)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code, shell commands, review decisions, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose fixes, record quality verdicts, and post GitHub pull-request reviews when run in PR-review mode.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
