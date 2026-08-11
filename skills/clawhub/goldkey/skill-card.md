## Description:

Evaluate and use GoldKey deterministic agent APIs for JSON canonicalization and validation, prompt-injection signal scanning, URL checks, spend-mandate checks, and Unicode normalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noah-ing](https://clawhub.ai/user/noah-ing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to query GoldKey live state, compare paygo and access-pass economics, and call deterministic utilities for JSON, security signal scanning, URL checks, spend-mandate checks, and Unicode normalization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some operations can involve USDC payments and unsigned transactions.

Mitigation: Use the live service response as the source of truth, require an explicit spend mandate before purchase-related actions, and review chain, contract, token, amount, calldata purpose, sequence, and expiry before signing.

Risk: Wallet signatures, short-lived access tokens, and delegated keys can expose account or API access if logged or shared.

Mitigation: Inject secrets through the agent secret store or standard input, write generated credentials only to private files, delete temporary secret files after import, and never pass signatures or tokens in command arguments.

Risk: Bulk delegated-key revocation can disrupt active child agents.

Mitigation: Use targeted key revocation unless intentionally rotating or disabling all delegated keys.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/noah-ing/skills/goldkey)
- [GoldKey API Origin](https://goldkey-edge-storefront.noah-ing.workers.dev)
- [GoldKey OpenAPI Schema](https://goldkey-edge-storefront.noah-ing.workers.dev/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide authenticated API calls, unsigned transaction review, and secret-handling workflows; it does not produce private keys or signed transactions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
