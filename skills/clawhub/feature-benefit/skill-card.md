## Description:

Connects Amazon product features to user benefits supported by review evidence and proposes listing-expression guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to translate product attributes into review-backed benefit statements for listing copy. It is intended for evidence mapping and listing guidance, not advertising bidding, unsupported product claims, or automatic publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can be steered outside the promised fixed workflow for paid remote analysis.

Mitigation: Review commands before execution, use the documented listing/benefits workflow only, and do not allow workflow or focus overrides unless the publisher documents and constrains them for this package.

Risk: The skill relies on ARI/Funewa for Amazon product identifiers, review-analysis requests, account-linked API key use, and credit-billed operations.

Mitigation: Use the skill only when ARI/Funewa is trusted for that data, and confirm quotes and request IDs before running paid operations.

Risk: Generated listing guidance could be incorrect, unsupported, or unsuitable for marketplace policy.

Mitigation: Treat output as a proposal and review it against the cited review evidence and applicable marketplace policy before using it in listing copy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/feature-benefit)
- [Amazon feature-benefit operation workflow](artifact/references/operation-workflow.md)
- [Amazon feature-benefit API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text or Markdown with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before credit-billed operations.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
