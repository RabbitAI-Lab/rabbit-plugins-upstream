## Description:

Helps agents manage MagicPay payments, funding, saved details, email, checkout choices, and payment recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent for purchases and account tasks can use MagicPay to prepare payments, request approval, fill checkout forms, manage saved details and email, and reconcile payment outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate real payments and checkout actions.

Mitigation: Review MagicPay approval and revocation settings; approve only intended purchases and reconcile the original operation before retrying.

Risk: Saved sensitive details and payment values may be exposed during assisted form filling.

Mitigation: Use only the authorized host-controlled collection and approval flows; avoid repeating sensitive values in replies or logs.

Risk: Provider discovery may introduce remote tools into purchase workflows.

Mitigation: Check the provider and purchase details before authorizing a transaction.

## Reference(s):

- [MagicPay ClawHub listing](https://clawhub.ai/xor777/skills/magicpay)
- [Skill homepage listed in metadata](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [MagicPay agent information](https://magiccard.ai/agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approval links and payment status; sensitive values should not be repeated in replies.]

## Skill Version(s):

0.4.95 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
