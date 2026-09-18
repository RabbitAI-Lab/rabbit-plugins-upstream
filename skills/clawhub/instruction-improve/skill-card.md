## Description:

Analyzes Amazon review questions about installation, use, and maintenance to identify evidence-backed improvements for product instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product teams, and support teams use this skill to convert Amazon review questions into prioritized instruction-improvement recommendations with supporting evidence. It is not intended for medical advice, legal advice, safety certification, compliance conclusions, or automatic publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can initiate paid ARI operations.

Mitigation: Use quote commands first, proceed only after explicit confirmation, and verify expected costs before running paid collection or analysis.

Risk: Security evidence rates the release as suspicious because broader workflow controls may be exposed beyond the dedicated instruction-improvement purpose.

Mitigation: Keep usage limited to the documented product/instructions workflow and avoid custom workflow or focus values unless intentionally using broader ARI capabilities.

Risk: Outputs are based on available review samples and may be incomplete if product data or review coverage is insufficient.

Mitigation: Treat findings as instruction-improvement guidance, check the cited review basis, and do not use the skill for medical, legal, safety-certification, compliance, or automatic publishing decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/instruction-improve)
- [Amazon instruction improvement workflow](references/operation-workflow.md)
- [Amazon instruction improvement API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, review evidence, conclusions, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid review collection or analysis must be quoted first and run only after explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
