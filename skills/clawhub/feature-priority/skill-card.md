## Description:

Combines Amazon review frequency, customer-experience impact, and product information to prioritize evidence-based product feature improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators, product teams, and marketplace consultants use this skill to rank product improvement opportunities from Amazon review evidence, ARI product data, and customer-impact signals. It is not intended for sales or profit forecasting, budget approval, procurement execution, or unsupported subjective prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key that can spend credits and change account settings.

Mitigation: Install only if the ARI service is trusted, keep auto-confirm disabled or limited when appropriate, and review schedule, watch, competitor, and account-setting changes before allowing them.

Risk: The release includes paid and persistent account-changing ARI workflows under a narrower feature-priority description.

Mitigation: Use quote-only requests for cost checks, require explicit confirmation for paid operations, and avoid unrelated account management workflows unless they are intentionally requested.

Risk: Export workflows can write files to user-selected paths.

Mitigation: Review export paths before writing and avoid paths that could overwrite important local files.

## Reference(s):

- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [README](artifact/README.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text guidance with occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid workflows may consume ARI credits after quote/confirmation or account auto-confirm rules.]

## Skill Version(s):

1.4.7 (source: server release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
