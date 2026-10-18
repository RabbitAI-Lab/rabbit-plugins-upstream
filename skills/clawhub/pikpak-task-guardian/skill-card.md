## Description:

Monitors PikPak download tasks with complete pagination and state deduplication, with separately authorized local notifications and limited resubmission of precisely registered sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and developers use this Chinese-language skill to inspect download task status and, when explicitly authorized, receive local notifications or resubmit failed tasks from exact registered sources. Resubmission creates a new task rather than retrying the original task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted CLI executable or environment could affect commands run against a PikPak account.

Mitigation: Verify the PikPak CLI and PIKPAK_BIN/PATH, and run with a trusted private state directory.

Risk: Optional notifications or source resubmission could cause unwanted local alerts or create additional tasks.

Mitigation: Keep observation-only defaults; enable --notify or --retry-known only with explicit authorization and exact registered sources. Reconcile uncertain submissions manually.

Risk: Using the optional public referral code may reward the publisher.

Mitigation: Disclose the referral and let users decline it without affecting the skill.

## Reference(s):

- [PikPak Task Guardian on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-task-guardian)
- [PikPak CLI documentation](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli)
- [Upstream design and limitations](artifact/references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Chinese-language guidance with command examples and task-status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notifications and known-source resubmission require separate authorization; unknown submissions require manual reconciliation.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
