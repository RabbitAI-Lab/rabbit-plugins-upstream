## Description:

Guides new PikPak users through manual installation, optional referral selection, account registration, and verification of a first cloud-download task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their assisting agents can follow a consent-based setup guide, review registration commands, and check a first cloud-download task by its returned ID. Registration, login, and downloads require the user's own actions and authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional referral code may benefit the guide's publisher.

Mitigation: Disclose the code and potential benefit before registration; use it only with the user's explicit consent.

Risk: Registration and download commands can affect an account or create cloud-download tasks.

Mitigation: Have the user review the account, link, and commands before running them; do not treat a command preview as completed registration.

## Reference(s):

- [PikPak CLI](https://mypikpak.com/cli)
- [PikPak CLI account registration guidance](https://mypikpak.com/en-US/help-center/connected_apps/pikpak_cli/register_account)
- [Onboarding design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and an optional JSON registration-command preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The preview prints commands for review; it does not register or log in.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
