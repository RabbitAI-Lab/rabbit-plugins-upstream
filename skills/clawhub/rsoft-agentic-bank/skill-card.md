## Description:

Helps autonomous agents check credit, request USDC loans, and repay them on Base mainnet through RSoft Agentic Bank.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rsoft-latam](https://clawhub.ai/user/rsoft-latam)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use this skill to check lending terms and credit, obtain signed USDC loans, manage human sponsorship, and repay loans on Base mainnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet credentials grant broad control over funds in the CDP project.

Mitigation: Use a dedicated CDP project and wallet with limited funds, and keep the wallet configuration outside synced folders.

Risk: Automatic loan, mailbox, or repayment actions can create unintended real-money obligations or transfers.

Mitigation: Require human review before running loan, mailbox, or repayment commands.

Risk: Repayment may send USDC to an unverified destination or for an incorrect amount.

Mitigation: Independently verify the repayment destination and amount; avoid the one-shot repayment script unless both are verified.

Risk: Unpinned dependencies may change behavior between installs.

Mitigation: Pin dependencies before installing or running the skill.

## Reference(s):

- [RSoft Agentic Bank website](https://rsoft-agentic-bank.com/)
- [RSoft Agentic Bank documentation](https://rsoft-agentic-bank.com/docs)
- [ClawHub skill release](https://clawhub.ai/rsoft-latam/skills/rsoft-agentic-bank)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Loan requests and repayments move real USDC on Base mainnet.]

## Skill Version(s):

2.4.0 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
