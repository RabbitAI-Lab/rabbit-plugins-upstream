## Description:

Coordinate shared Todo tasks and consolidated reminders across Hermes, OpenClaw, ChatGPT/Codex, WorkBuddy, and other agents through Git.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ernest-su](https://clawhub.ai/user/ernest-su)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate tasks, delegation, lifecycle updates, and consolidated reminders across multiple agent hosts through a shared Git repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires shell access to run the bundled Python CLI and Git access to the shared todo repository.

Mitigation: Install only where that access is acceptable, use a dedicated repository, and rely on the host's normal Git credential mechanism.

Risk: Task text and Git commits can expose secrets, private transcripts, or sensitive operational details if users place them in todo records.

Mitigation: Do not store tokens, passwords, SSH keys, messaging credentials, private transcripts, or other secrets in task files or commits.

Risk: Git synchronization is eventually consistent and is not a transactional queue or lock service.

Mitigation: Sync before decisions and writes, preserve executor ownership, and use a real database or queue for strong consistency or high-frequency competing-worker workflows.

Risk: Reminder delivery is at-least-once, so failed receipt publishing or overlapping notifier runs can repeat reminders.

Mitigation: Designate one active notifier, avoid overlapping notifier runs, and record receipts only after the combined reminder is successfully delivered.

## Reference(s):

- [Runtime compatibility](references/compatibility.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash examples; CLI responses are JSON objects and managed task and receipt files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Git, Python 3.10+, shell execution, and access to a shared Git repository.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
