## Description:

Guides new PikPak users through self-installation, informed referral choice, browser registration and login, and verification of a first cloud download by task ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their assisting agents use this guide to review CLI setup, choose whether to use a disclosed referral code, and check the status of an authorized first cloud download. Registration and login remain user-driven.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The public referral code may benefit the guide's publisher.

Mitigation: Disclose the code and potential benefit before registration; use it only after an explicit choice, and allow registration without a referral.

Risk: Account operations or cloud downloads could affect the wrong account or add unauthorized content.

Mitigation: Confirm account ownership and authorization before account commands, submit only links the user is allowed to use, and verify the resulting task by its exact ID.

## Reference(s):

- [PikPak CLI installation](https://mypikpak.com/cli)
- [PikPak CLI registration guidance](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli/register_account)
- [Onboarding design and verification boundaries](references/upstream-design.md)
- [PikPak Onboarding on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON command preview]

**Output Format:** [Markdown guidance and optional JSON registration-command preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registration preview does not execute commands; task status requires checking the returned task ID.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
