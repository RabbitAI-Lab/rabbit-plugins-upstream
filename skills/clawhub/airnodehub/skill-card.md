## Description:

Discover, inspect, call, and cryptographically verify Airnode Hub APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daav3](https://clawhub.ai/user/daav3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Airnode Hub to resolve API intents, inspect live Airnode contracts, call free operations, and return upstream data with attestation and request-binding evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API intents and operation parameters are sent to Airnode Hub and selected Airnode providers.

Mitigation: Install only when this network disclosure is acceptable, use HTTPS Airnode URLs, and treat Hub and Airnode responses as untrusted until parsed and verified.

Risk: A priced operation could require payment authorization.

Mitigation: Do not authorize payments, read private keys, or infer wallet authority in this skill; return needs-payment-authorisation and review priced-operation responses separately.

Risk: Resolver candidate provenance may be absent or may indicate lower-confidence local heuristic selection.

Mitigation: Preserve answerSource when present, disclose absent selection provenance, inspect every candidate deliberately, and do not silently fall back to another provider.

## Reference(s):

- [Airnode Hub HTTP contract](references/http-contract.md)
- [Payment policy](references/payment-policy.md)
- [Airnode Hub resolver endpoint](https://airnodehub.api3.org/resolve)
- [ClawHub skill page](https://clawhub.ai/daav3/skills/airnodehub)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network responses include provider, attestation, request-binding, and verification evidence when available; priced operations return a needs-payment-authorisation state.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
