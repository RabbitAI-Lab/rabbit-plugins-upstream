## Description:

Turn written account-opening steps into one account opening voice clip per labeled cue. This account opening guidance studio records each teller guidance clip and KYC step voice from the steps the desk already wrote, then delivers 8 to 20 account opening audio files. Use it for brokerage onboarding audio that keeps one step on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External brokerage, onboarding, and branch teams use this skill to turn their already-written account-opening steps into a labeled set of short voice clips for customer guidance. It supports KYC and teller guidance workflows while requiring pronunciation input, voice rights for cloning, and confirmation before paid speech or clone calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad shared Beatra authorization can grant access across multiple media, wallet, task, voice, and artifact capabilities.

Mitigation: Review requested scopes before authorizing, keep the device token private, and use this skill only where a shared Beatra credential is acceptable.

Risk: Silent self-updates can change package behavior after installation.

Mitigation: Disable automatic updates in managed or regulated environments and run manual update checks only after review.

Risk: Paid clone and speech requests can create charges or duplicate work if replayed incorrectly.

Mitigation: Confirm each paid stage, use one opaque client_request_id per logical request, and retry only with byte-identical arguments when delivery is uncertain.

Risk: Voice cloning can misuse likeness if rights are missing or assumed from file access.

Mitigation: Require explicit likeness and voice rights before cloning and inspect only authorized samples.

## Reference(s):

- [Account opening voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Audio files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and MP3 audio task outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled list and typically 8 to 20 account-opening voice clips; paid clone and speech stages require confirmation, live pricing, and opaque client_request_id tracking.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
