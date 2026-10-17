## Description:

Audits PikPak shares for known expired, soon-to-expire, and zero-view items and provides read-only reports and guidance for separately authorized share management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and their authorized assistants use this skill to review share-list expiration and view data in a private report and decide whether any shares warrant manual follow-up. The audit does not create, delete, or revoke shares.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads a private PikPak share list and produces a report containing account metadata.

Mitigation: Authorize account access first, use a trusted runtime, and keep the local report private.

Risk: Missing or unverified share fields may make expiration and view classifications incomplete.

Mitigation: Treat unknown values as unknown and review share IDs and live account data before taking action.

Risk: Manual share changes or referral-code use can affect an account or benefit the publisher.

Mitigation: Approve create or revoke actions separately; explicitly decline or clear the disclosed referral code if unwanted.

## Reference(s):

- [Share audit design and upstream research](artifact/references/upstream-design.md)
- [PikPak Share Manager release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-share-manager)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text audit summary and optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes audit timestamps, share IDs, and flags for manual review; the report contains private account metadata.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
