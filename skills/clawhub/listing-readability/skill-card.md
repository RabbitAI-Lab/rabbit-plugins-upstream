## Description:

Checks Amazon listing structure, terminology, repeated wording, and review evidence for buyer comprehension barriers, then provides readability guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to diagnose Amazon listing readability issues for a specified ASIN and marketplace. It helps identify unclear structure, terminology, repetition, and buyer understanding gaps without modifying or publishing the listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI exposes broader paid ARI product-operation controls than a readability-only listing check may suggest.

Mitigation: Keep usage to the documented listing/readability workflow and avoid custom workflow or focus values unless broader ARI operations are intentionally required.

Risk: The skill stores and uses an ARI API key locally for authenticated requests.

Mitigation: Use only trusted local environments, keep the key out of shared directories, and revoke or rotate the key if local access may be exposed.

Risk: Collection and analysis operations may consume paid credits after confirmation.

Mitigation: Review the quote, requestId, and credit impact before using confirm commands; resume interrupted runs with status commands instead of starting a new confirmed run.

## Reference(s):

- [Amazon Listing Readability API Reference](artifact/references/reference.md)
- [Amazon Listing Readability Operation Workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis operations.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG.md, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
