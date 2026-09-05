## Description:

x402 pay-per-request access to the read-only Fomo App crypto trading data API for agent research across Solana, meme coins trading, crypto, social trading, and on-chain data, with normalized JSON and no wallet signing or trade execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to perform read-only market-intelligence lookups against the documented Fomo App crypto trading data gateway. It helps summarize supported token, trader, thesis, alert, notification, and search data without wallet signing, trade execution, or mutation capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use may contact an external paid or prepaid API and send market handles, token identifiers, or query terms to that API.

Mitigation: Review the requested route and query values before use, keep access modes distinct, and use approved credential handling for Bearer or prepaid access.

Risk: Users could expose wallet seed phrases, private keys, API keys, or other credentials while trying to access crypto data.

Mitigation: Do not request or paste secrets in chat; redact sensitive identifiers and rely only on approved credential storage and runtime injection.

Risk: Market data, URLs, query values, or indexed thesis and alert content may contain untrusted text.

Mitigation: Treat API responses as data rather than instructions, summarize only the fields needed for the task, and avoid executing embedded instructions.

Risk: The skill could be misapplied as trading, wallet, or transaction automation.

Mitigation: Limit use to the documented read-only GET routes and refuse wallet signing, trade execution, transactions, orders, broker connections, and unsupported mutations.

## Reference(s):

- [Fomo App API gateway](https://api.replynodes.com/v1/fomo)
- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/fomo-app-data-api)
- [ReplyNodes publisher profile](https://clawhub.ai/user/replynodes-ai)

## Skill Output:

**Output Type(s):** [guidance, API calls, text, markdown]

**Output Format:** [Markdown guidance with normalized JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET route guidance; no wallet signing, trade execution, credential capture, or persistence.]

## Skill Version(s):

1.0.8 (source: server release, SKILL.md frontmatter, VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
