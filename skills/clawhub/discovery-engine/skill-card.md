## Description:

Automatically discovers novel, statistically validated patterns in tabular data, including feature interactions, subgroup effects, and conditional relationships, with hold-out validation, FDR-corrected p-values, citations, and novelty scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and data-science teams use this skill to run Disco on tabular datasets, choose a target column, exclude leakage or tautological columns, and retrieve statistically validated pattern findings with report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Datasets may be sent to Disco/cloud storage for analysis.

Mitigation: Use the skill only for data that policy permits sending to Disco/cloud storage, and avoid sensitive datasets unless private mode and organizational approval are in place.

Risk: Analyses can be published by default.

Mitigation: Confirm the intended visibility before each run and explicitly choose private mode for non-public data.

Risk: A locally running integration can upload arbitrary readable local files.

Mitigation: Restrict uploads to user-selected dataset paths and require confirmation before uploading or analyzing a local file.

Risk: The skill exposes account, API-key, payment-method, credit-purchase, and subscription workflows.

Mitigation: Require human confirmation before account creation, API-key handling, payment-method attachment, credit purchases, or subscription changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Python SDK Documentation](docs/python-sdk.md)
- [OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown explanations with structured pattern fields, API tool calls, setup commands, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DISCOVERY_API_KEY. Results can include pattern descriptions, conditions, effect sizes, p-values, citations, novelty labels, feature importance, and report URLs.]

## Skill Version(s):

0.2.178 (source: pyproject.toml, server.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
