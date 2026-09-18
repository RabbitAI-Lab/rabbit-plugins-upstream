## Description:

Creates a comparative matrix of Amazon product features using product fields and review evidence, while flagging evidence gaps and experience differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to compare a primary ASIN with authorized competitors, summarize feature differences from product fields and review evidence, and identify missing data before acting on the analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced CLI flags could request server-supported product-operation workflows beyond the advertised competitor-feature matrix.

Mitigation: Install only where the fixed page_compare/features workflow is acceptable, and rely on backend or wrapper enforcement to reject unsupported workflow or focus overrides.

Risk: The skill requires an ARI API key, may store it locally when configured, and sends ASIN or account-related requests to ari.funewa.com.

Mitigation: Use the documented ARI setup or configure flow, review local credential handling, and keep API and authorization traffic on the official ari.funewa.com endpoint.

Risk: ARI credits can be spent on paid collection or analysis after explicit confirmation.

Mitigation: Run profile and quote steps first, preserve the quoted requestId, and execute paid run or collect commands only after the user confirms the quoted cost.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-features)
- [Amazon competitor feature matrix workflow](references/operation-workflow.md)
- [Amazon competitor feature matrix API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text analysis with quoted CLI commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis should run only after quote review and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
