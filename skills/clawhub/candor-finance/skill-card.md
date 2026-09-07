## Description:

Use Candor to organize personal-finance accounts and spending, remember approved budgets and goals, review investments, investigate possible savings, and keep evidence and follow-up together.

This skill is ready for commercial/non-commercial use.

## Publisher:

[candor](https://clawhub.ai/user/candor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work with an authenticated Candor workspace for personal-finance review, planning, record cleanup, and follow-up while keeping consent and external-action boundaries visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can work with sensitive personal-finance records through an authenticated Candor workspace.

Mitigation: Install it only when the user intends to use Candor for this purpose, keep Candor authentication under the user's control, and avoid exposing credentials, payment details, or verification codes in chat.

Risk: Optional background monitoring could create continuing financial review activity beyond the immediate conversation.

Mitigation: Enable monitoring only after the user explicitly chooses a cadence and purpose, and verify that the configured environment can run authenticated Candor checks.

Risk: External financial actions can affect money, accounts, filings, trades, or third-party communications.

Mitigation: Treat Candor workspace access as information access only; require separate recoverable or fresh authority before payments, transfers, cancellations, filings, trades, messages, or similar external actions.

## Reference(s):

- [Candor Finance start](https://candor.money/START.md?v=0.1.59)
- [Quiet monitoring recipes](references/monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command recipes and concise financial findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Candor workspace and Candor CLI 0.3.94 or newer; external payments, transfers, cancellations, filings, trades, and messages require separate authority.]

## Skill Version(s):

0.1.59 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
