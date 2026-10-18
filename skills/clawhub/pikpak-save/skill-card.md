## Description:

Guides manual PikPak link saves and selective share restores, with a local checker for task receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their assisting agents use this skill to submit authorized links, check tasks by exact ID, and restore selected files from shares. A local checker examines task receipts; the workflow does not provide a persistent queue or automatic retries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A save or restore may target the wrong account, folder, or shared files.

Mitigation: Confirm the current account and target folder before each action, and restore only explicitly approved file IDs.

Risk: Retrying after an uncertain result can duplicate a task or restore.

Mitigation: Record the exact task ID and reconcile uncertain results before authorizing another creation or restore.

Risk: Share passwords, login details, or a referral code may be exposed or used unintentionally.

Mitigation: Keep passwords and login steps in the user's terminal, and review the disclosed referral code before registration.

## Reference(s):

- [Upstream design and limitations](references/upstream-design.md)
- [rclone PikPak task lookup and wait reference](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/helper.go#L186-L215)
- [GitHub CLI login-flow reference](https://github.com/cli/cli/blob/3d7967df5a94052b0554898ffa02526f0f90b8c9/pkg/cmd/auth/shared/login_flow.go#L204-L210)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON task status]

**Output Format:** [Markdown instructions and JSON from the optional local receipt checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual confirmation is required; no persistent task ledger or automatic retries.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
