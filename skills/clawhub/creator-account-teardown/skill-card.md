## Description:

Creator Account Teardown reads a creator account from supplied evidence or supported public lookups, diagnoses its positioning and content patterns, and turns the result into a build template and first post with generated cover and narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and operators use this skill to benchmark a creator or competitor account, identify visible positioning and content patterns, and create their own account plan and first post assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media, tool, and wallet-spending authority.

Mitigation: Install only after reviewing Beatra account permissions and keep revocation and disconnect controls available before running billable work.

Risk: Public social lookups, selected uploads, and generated media requests are sent to Beatra.

Mitigation: Use pasted account evidence when remote lookup is unnecessary, avoid submitting sensitive media, and label which information came from the user versus a lookup.

Risk: Optional social lookups and production steps can incur separate charges.

Mitigation: Confirm each lookup and each production call separately with the current price and a stable request identifier before execution.

Risk: Automatic updates are enabled by default and can replace package-owned code.

Mitigation: Consider disabling automatic updates with the documented update command and use explicit update checks when stricter change control is needed.

Risk: Account metrics and performance explanations can be stale, incomplete, or inferential.

Mitigation: Carry source labels and read times for looked-up data, avoid estimating missing metrics, and mark performance explanations as inference.

## Reference(s):

- [Creator Account Teardown ClawHub Listing](https://clawhub.ai/beatra-ai/skills/creator-account-teardown)
- [Beatra Skill Homepage](https://beatra.ai/skills/creator-account-teardown)
- [Reading the account](references/account-read.md)
- [Reading the account from a handle](references/account-lookup.md)
- [Building your own account](references/build-template.md)
- [Account teardown workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with evidence tables, structured analysis, inline shell commands, and returned artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image and audio artifact links after separately approved paid Beatra tasks complete.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
