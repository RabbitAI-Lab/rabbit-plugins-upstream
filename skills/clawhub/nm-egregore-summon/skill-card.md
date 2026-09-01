## Description:

Autonomous orchestrator for manifest work items through the development lifecycle

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to process manifest-backed work items through intake, build, quality, and ship stages while preserving state across retries, context limits, and rate-limit cooldowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous runs can continue, re-enter themselves, and modify repository state with limited user control.

Mitigation: Use bounded mode, review .egregore state before launch, and delete scheduled cron recovery when the run should stop.

Risk: Automated merge behavior can land repository changes with limited oversight.

Mitigation: Keep auto_merge disabled unless protected-branch review is already enforced.

Risk: Untrusted GitHub issues can steer an autonomous repository workflow.

Mitigation: Avoid feeding untrusted GitHub issues without supervision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-summon)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore)
- [Publisher profile](https://clawhub.ai/user/athola)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline commands and structured workflow state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke other skills and repository commands while advancing manifest work items.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
