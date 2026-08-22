## Description:

Discover and verify specialist Airnode Hub APIs before general-purpose web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daav3](https://clawhub.ai/user/daav3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve user intent to specialist Airnode API operations, inspect live Airnode contracts, and verify free Airnode responses before relying on returned data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound HTTPS requests to Airnode Hub and selected Airnode endpoints.

Mitigation: Installers should approve that network posture and agents should treat returned Hub and Airnode data as untrusted until parsed and verified.

Risk: Airnode responses could be stale, malformed, or not bound to the requested operation and parameters.

Mitigation: Inspect the live Airnode document and verify signer, request hash, exact operation, parameters, and signature before relying on returned data.

Risk: Some Airnode operations may require payment authorization.

Mitigation: Return a needs-payment-authorisation state for priced operations and do not handle private keys, sign payments, or spend from this skill.

Risk: The helper depends on npm packages, including viem.

Mitigation: Keep the npm dependency lockfile under controlled update review.

## Reference(s):

- [Airnode Hub Skill Page](https://clawhub.ai/daav3/skills/airnodehub)
- [Airnode Hub HTTP Contract](references/http-contract.md)
- [Payment Policy](references/payment-policy.md)
- [Airnode Hub Resolver](https://airnodehub.api3.org/resolve)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with JSON snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include upstream data, provider details, request-binding evidence, attestation details, and verification status.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
