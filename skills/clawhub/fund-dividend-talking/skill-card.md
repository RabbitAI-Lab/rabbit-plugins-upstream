## Description:

Turns a user-supplied fund dividend announcement and authorized stills into short, individually narrated talking clips, one per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors and fund marketers use this skill to plan and produce separate short talking clips from an existing dividend announcement and stills they are authorized to use. The spoken claims stay within the supplied announcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants broad account access, including media, tasks, wallet information, and credit spending.

Mitigation: Approve access only for a trusted account, confirm each paid stage, monitor credit usage, and revoke the device when access is no longer needed.

Risk: The installed skill can update its package files automatically without a separate prompt.

Mitigation: Review the update policy and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if silent changes are unacceptable.

Risk: Generated financial narration may misstate dividend facts or imply an unannounced account credit.

Mitigation: Check every spoken line and delivered clip against the supplied announcement; do not invent dates, amounts, yields, or investment recommendations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/fund-dividend-talking)
- [Dividend talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Video clips]

**Output Format:** [Labeled Markdown clip plan and individual generated video assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per approved still; reports available media details and net credits charged.]

## Skill Version(s):

0.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
