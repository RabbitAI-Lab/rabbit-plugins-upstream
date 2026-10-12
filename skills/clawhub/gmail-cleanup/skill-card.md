## Description:

Triage Gmail into spam, informational, and action-needed lanes, propose cleanup and reply drafts, and apply approved changes after Telegram review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeyang001](https://clawhub.ai/user/joeyang001)

### License/Terms of Use:

MIT-0

## Use Case:

Gmail account owners use this skill to review inbox triage and draft replies in Telegram before approving mailbox cleanup or sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad search or mistaken classification could include important mail in cleanup proposals.

Mitigation: Review the Gmail query, lane policies, proposed actions, and per-run action cap; inspect the dry-run before applying changes.

Risk: Drafts or mailbox actions could affect recipients or remove messages unexpectedly.

Mitigation: Verify the approved action list and Telegram recipient; require explicit approval before applying actions and separate approval before sending drafts.

Risk: The Gmail keyring password may be exposed if stored insecurely.

Mitigation: Supply GOG_KEYRING_PASSWORD only for the run through a session or secret manager; do not persist or commit it.

## Reference(s):

- [gmail-cleanup on ClawHub](https://clawhub.ai/joeyang001/skills/gmail-cleanup)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Triage summaries and reply drafts, Telegram approval digests, and JSON action proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox changes require an approval artifact and explicit apply step; sends require separate approval.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
