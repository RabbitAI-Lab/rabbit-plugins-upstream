## Description:

Guides new PikPak users through self-managed setup, informed referral choice, browser registration, and verification of a first cloud download by task ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and assistants use this guide to plan account setup and verify a user-authorized cloud download without handing credentials to the assistant or assuming account identity from login status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The disclosed referral code may benefit the guide's publisher.

Mitigation: Explain the referral before registration, obtain an explicit choice, and check the registration page before submitting.

Risk: Account actions may affect the wrong account or expose credentials.

Mitigation: Confirm the current account and authorization before status or task commands; keep credentials with the user.

Risk: Creating a cloud download task can write to the account and consume quota.

Mitigation: Confirm the link and destination first, then track the exact returned task ID without assuming a timed-out request failed.

## Reference(s):

- [PikPak Onboarding on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-onboarding)
- [PikPak CLI installation](https://mypikpak.com/cli)
- [PikPak CLI registration policy](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli/register_account)
- [Upstream design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands; optional JSON registration plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The registration plan is a preview; the user performs registration and confirms account actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
