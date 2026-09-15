## Description:

Checks whether Amazon listing promises about product functions, effects, and usage are supported by customer review evidence, and identifies evidence gaps without producing legal compliance conclusions or publishing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to compare Amazon listing claims against collected review feedback before deciding whether the claims have enough evidence support. It is intended for evidence review and gap identification, not legal compliance decisions or automatic listing edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged CLI can run paid product-operation workflows beyond the fixed listing-promise scope described to users.

Mitigation: Review generated commands before execution, keep workflow and focus aligned to listing/promise, and require explicit user confirmation before paid runs.

Risk: The skill stores a reusable ARI API key locally.

Mitigation: Install only when the ARI service is trusted, protect the local environment where the key is stored, and rotate or revoke the key if exposure is suspected.

Risk: Outputs may overstate conclusions if review evidence is insufficient.

Mitigation: Treat results as evidence-gap analysis, preserve data-scope caveats, and avoid using the skill for legal compliance conclusions or automatic Amazon listing changes.

## Reference(s):

- [Amazon Listing Promise API Reference](references/reference.md)
- [Amazon Listing Promise Operation Workflow](references/operation-workflow.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and review-evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid runs.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
