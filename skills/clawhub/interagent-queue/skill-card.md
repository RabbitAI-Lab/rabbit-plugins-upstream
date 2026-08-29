## Description:

Deprecated under the name interagent-queue, this skill observes a miab-broker ledger, writes human-readable callback logs, and can send configured closed-bottle summaries to chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albzhu](https://clawhub.ai/user/albzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators using miab-broker use this skill to monitor callback ledger activity, keep local human-readable logs, and optionally route closed-bottle summaries to a configured chat target during migration to miab-observer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger text can be relayed into chat as written when closed-bottle notifications are enabled.

Mitigation: Set CLAW_CLOSED_TARGET deliberately, review notify_closed_dryrun.py output first, and avoid routing untrusted ledger content to channels where mentions or deceptive formatting would be disruptive.

Risk: Cron jobs that keep calling the old interagent_queue.py path can stop working after migration.

Mitigation: Install miab-observer 2.0.0, update cron command paths to the renamed script, and confirm state files still point at the intended CLAW_HOME and LYRA_WORKSPACE before removing interagent-queue.

Risk: Operator recovery from an unusable cursor state can replay historical ledger entries if the state file is deleted intentionally.

Mitigation: Inspect and repair last_processed_line when possible; delete the state file only when accepting a full replay is appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/albzhu/skills/interagent-queue)
- [Publisher profile](https://clawhub.ai/user/albzhu)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON status responses, Markdown-style log entries, and configured chat messages from local Python CLI scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads miab-broker ledger state; notification delivery requires CLAW_CLOSED_TARGET and delegates egress to openclaw message send.]

## Skill Version(s):

1.3.0 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
