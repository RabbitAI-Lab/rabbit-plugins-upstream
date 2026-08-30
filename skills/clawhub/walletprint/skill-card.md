## Description:

WalletPrint screens proposed crypto transactions against a sender wallet's behavioral history and returns an advisory risk score, band, and reason codes before signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loai17](https://clawhub.ai/user/loai17)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use WalletPrint before signing or submitting crypto transactions to flag anomalous transfers and route medium- or high-risk activity into their own approval workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed wallet transaction details are sent to WalletPrint and should be treated as sensitive.

Mitigation: Confirm user consent and compliance requirements before production use, and decide whether production persistence and history seeding are acceptable.

Risk: WalletPrint is advisory and does not block or approve transactions.

Mitigation: Add an approval gate before signing high-risk transactions and keep final execution decisions in the integrator's workflow.

Risk: Webhook delivery can expose transaction alerts to external automation endpoints.

Mitigation: Configure webhooks only to trusted HTTPS endpoints and route alerts through controlled approval systems.

Risk: Free-form feedback notes may contain sensitive information.

Mitigation: Avoid entering secrets, private user data, or unnecessary transaction context in feedback notes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/loai17/skills/walletprint)
- [Server-resolved GitHub Repository](https://github.com/Loai17/walletprint-sdk)
- [npm Package](https://www.npmjs.com/package/@walletprint/sdk)
- [Getting Started](docs/getting-started.md)
- [HTTP API Reference](docs/api.md)
- [Approval Flow and Webhooks](docs/approval-flow.md)
- [Compliance and Audit Export](docs/compliance.md)
- [Dashboard and API Keys](https://walletprint.vercel.app/dashboard/signup)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript and shell examples, plus JSON score and feedback shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory only; scoring responses include a 0-100 score, low/medium/high band, plain-English reason codes, and optional screened transaction identifiers.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
