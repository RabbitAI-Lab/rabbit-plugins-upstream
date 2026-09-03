## Description:

Run 15 to 400+ social accounts without burning them by helping operators manage bulk scheduling, per-account caption variation, per-account results, platform restrictions, token recovery, spam limits, and account-count economics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackfriks](https://clawhub.ai/user/jackfriks)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators, agencies, and creators use this skill to run many Post Bridge-connected social accounts while spacing posts, interpreting per-account failures, and recovering from common token, quota, media, and platform restriction issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-suggested posting, scheduling, media deletion, or multi-account commands can affect public social accounts.

Mitigation: Review proposed Post Bridge CLI commands before execution, especially commands that create posts, schedule batches, or delete media.

Risk: Republishing after transient platform errors can create duplicate posts when a platform reports failure after publishing.

Mitigation: Check the affected account's live post state before retrying failed Instagram or other transient platform results.

Risk: Continuing to schedule restricted accounts can waste attempts and prolong account health issues.

Mitigation: Pause restricted account queues, wait for the platform restriction to clear, and resume at a lower posting frequency.

## Reference(s):

- [Post Bridge API reference](https://api.post-bridge.com/reference)
- [Post Bridge agent-mode freshness reference](https://github.com/post-bridge-hq/agent-mode)
- [ClawHub release page](https://clawhub.ai/jackfriks/skills/multi-account-operator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend Post Bridge CLI commands for account listing, media upload, post creation, result inspection, analytics, and media deletion.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
