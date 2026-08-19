## Description:

Defines a multi-agent teamwork protocol for OpenClaw, including coordinator scheduling, task handoff, audit fallback, notifications, and immediate repository push expectations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[managernet](https://clawhub.ai/user/managernet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate OpenClaw multi-agent work through task files, scheduling rules, audit checks, and human notification paths. It is most relevant where agents are expected to divide work, preserve execution state, and push completed work to a repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous scheduled agents may modify task state, archive files, notify external recipients, and push repository changes without clear approval boundaries.

Mitigation: Install only in repositories where that autonomy is permitted, or require human approval, protected branches, recipient allowlists, and redaction rules before enabling the workflow.

Risk: External notifications may expose task details or sensitive context to unintended DingTalk or email recipients.

Mitigation: Use recipient allowlists, validate notification IDs against a trusted team directory, and redact secrets or sensitive project details from notification payloads.

Risk: Immediate commit-and-push expectations can publish incorrect or unwanted changes if agents act without review.

Mitigation: Route agent commits through protected branches, pull requests, or other human review gates in shared and sensitive repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/managernet/skills/teamwork)
- [Publisher profile](https://clawhub.ai/user/managernet)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with task-schema examples, scheduling tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for coordinating agents; does not itself execute the described cron, notification, git, or repository workflows.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
