## Description:

Provides pay-per-call market intelligence through x402 on Base and Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lacryptorina](https://clawhub.ai/user/lacryptorina)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Vedetta to retrieve free, cached, or paid descriptive market analysis for crypto, US stocks, and macro indicators. The skill is intended for research reads, not trade execution, custody, or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a payment signing flow without a documented price ceiling, and scan coverage is partial.

Mitigation: Review the payment setup and set an acceptable spend limit before use. Confirm each payment offer, abort amounts above the documented tier, and use a dedicated low-balance wallet.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lacryptorina/skills/vedetta-skill)
- [Vedetta service and API](https://vedetta.dethboy.com)
- [Vedetta installation instructions](https://vedetta.dethboy.com/install)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON market data and analyst text; Markdown instructions with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market research; one ticker per API call; some routes require paid x402 requests.]

## Skill Version(s):

2.14.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
