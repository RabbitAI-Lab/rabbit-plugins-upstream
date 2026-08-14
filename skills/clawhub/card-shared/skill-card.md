## Description:

Shared research policy and output contracts for the card command suite (card-full, card-transfer, card-rate, card-news, card-credits, card-compare, card-value, card-wallet, and card-profile-recommend).

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

Agent developers and card-command agents use this hidden shared skill as background reference for credit-card research policy, source selection, confidence handling, output contracts, and composition rules across the card command suite.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The bundled PDF helper can install dependencies and launch an unsandboxed browser if run.

Mitigation: Review the helper before use; pin dependency installation and harden the browser invocation by removing --no-sandbox, avoiding broad remote origins, and using a safer debugging setup.

## Reference(s):

- [Card Shared Rules on ClawHub](https://clawhub.ai/jiahongc/skills/card-shared)
- [source-policy.yaml](artifact/source-policy.yaml)
- [command-contracts.yaml](artifact/command-contracts.yaml)
- [section-definitions.md](artifact/section-definitions.md)
- [card-identity-rules.md](artifact/card-identity-rules.md)
- [confidence-rules.md](artifact/confidence-rules.md)
- [recency-rules.md](artifact/recency-rules.md)
- [normalization-rules.md](artifact/normalization-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with internal YAML contracts and supporting configuration or scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing card command outputs are compact Markdown; sources and confidence notes are kept in hidden YAML according to the shared contract.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
