## Description:

Workflow Guard Rails adds pre-execution checks, checkpointing, side-effect queues, retry budgets, result validation, audit logs, and failure-rule accumulation around multi-step agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to wrap scheduled or side-effectful agent workflows with checks that reduce false success, duplicate external actions, unrecoverable crashes, and silent drift. It is most relevant when workflows send, publish, pay, delete, write to another system, or need safe reruns after a mid-task failure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents to write lasting guidance into ~/.workbuddy/ERROR-PLAYBOOK.md without prior approval.

Mitigation: Use a project-scoped path, require explicit approval or a staging queue before persistent rule updates, and review rollback paths before unattended use.

Risk: The companion playbook is bootstrapped from an unpinned raw URL.

Mitigation: Pin and verify the companion playbook content before installation, preferably by storing an expected version or hash with the deployment.

## Reference(s):

- [Guardian Patterns](artifact/references/guardian-patterns.md)
- [Companion Error Playbook](https://raw.githubusercontent.com/haiyangchenbj/error-playbook/main/ERROR-PLAYBOOK.md)
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/workflow-guard-rails)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance and Guardian Report checklist with occasional bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct agents to maintain checkpoints, queue side effects until validation passes, and append confirmed failures to ~/.workbuddy/ERROR-PLAYBOOK.md.]

## Skill Version(s):

1.0.5 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
