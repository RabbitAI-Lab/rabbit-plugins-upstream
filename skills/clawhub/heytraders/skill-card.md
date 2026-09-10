## Description:

Operate HeyTraders through the live heytraders_cli browser command catalog when the user asks to inspect, navigate, configure, or manage the HeyTraders application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heytraders](https://clawhub.ai/user/heytraders)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HeyTraders through the live browser command catalog for inspection, navigation, configuration, exchange onboarding, and application management. It is designed to preserve live command schemas, browser handoffs, and explicit authority boundaries for financial actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide operation of a financial trading application where orders, strategy starts, wallet approvals, credential changes, deposits, or other irreversible actions may carry financial risk.

Mitigation: Require explicit confirmation for irreversible actions and re-read affected state before claiming success.

Risk: The skill depends on a separate HeyTraders OpenClaw plugin and browser transport that users must trust and enable.

Mitigation: Verify the HeyTraders plugin publisher and package version before installation, use a dedicated browser profile, and keep exchange/API permissions minimal.

Risk: Exchange credentials, private keys, seed phrases, cookies, tokens, or wallet material could be mishandled if entered into chat or command arguments.

Mitigation: Enter secrets only through the secure browser or venue surface identified by the live guide; never pass secret material through heytraders_cli arguments or chat.

## Reference(s):

- [HeyTraders skill page](https://clawhub.ai/heytraders/skills/heytraders)
- [HeyTraders OpenClaw package installation guide](https://github.com/heytraders/HeyTraders-OpenClaw/blob/develop/README.md#install-in-an-existing-openclaw-environment)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live command discovery through heytraders_cli and preserves structured errors, handoffs, and confirmation requirements.]

## Skill Version(s):

2.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
