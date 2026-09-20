## Description:

Razorpay helps agents operate Razorpay through an OOMOL-connected account for order, payment, and refund workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Razorpay action schemas and run order, payment, and refund operations against an OOMOL-connected Razorpay account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate high-impact financial actions such as order creation and refunds.

Mitigation: Confirm every write or refund payload and its expected effect with the user before execution.

Risk: The setup guidance includes remote CLI installation scripts.

Mitigation: Use a verified, reviewed installation method for the oo CLI instead of running remote install scripts blindly.

## Reference(s):

- [ClawHub Razorpay skill page](https://clawhub.ai/oomol/skills/oo-razorpay)
- [Razorpay homepage](https://razorpay.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Markdown with bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce JSON responses from Razorpay connector actions.]

## Skill Version(s):

1.0.4 (source: server release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
