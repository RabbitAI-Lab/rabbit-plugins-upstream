## Description:

Reviews local agent-action logs as a timestamped ledger and flags certain ungated write actions for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and auditors use this skill to review agent-action logs, reconstruct a timeline, and identify possible ungated writes for manual investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation lists command options and a script path that do not match the bundled command.

Mitigation: Check the bundled command's help and use --log with a specific log you intend to review.

Risk: Automated flags alone may not establish whether an action was authorized.

Mitigation: Check flagged and unflagged entries against the original log and permission records before drawing compliance conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-trace-audit)
- [LGD theory (linked background, not source provenance)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text action timeline and count of flagged writes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads a user-selected local JSONL log; command output is in Chinese and does not create an archive.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
