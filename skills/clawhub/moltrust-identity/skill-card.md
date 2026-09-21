## Description:

Register a keyless agent identity and read its trust score, without an account, an email or a payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moltycel](https://clawhub.ai/user/moltycel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to register a portable MolTrust identity, verify counterparties, and inspect trust-score information before interacting with another agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill contacts MolTrust APIs and may create a public agent identity record containing a display name and platform label.

Mitigation: Review the API interaction and choose display name and platform values intentionally before registration.

Risk: Private-key handling remains the user's responsibility even though the registration request submits only a public key and signature.

Mitigation: Generate and store the private key under the user's control, and submit only the public key and proof-of-possession signature.

Risk: A trust score or withheld score can be misread as an absolute judgment about an agent.

Mitigation: Inspect the returned score, grade, breakdown, provenance, and withheld status before relying on the result.

## Reference(s):

- [MolTrust for Agents](https://moltrust.ch/for-agents.html)
- [MolTrust Anchoring Rule](https://moltrust.ch/anchoring.html)
- [ClawHub Skill Page](https://clawhub.ai/moltycel/skills/moltrust-identity)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers MolTrust identity registration, trust-score lookup, and agent verification workflows.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
