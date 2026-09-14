## Description:

Plans the information that Amazon main and supporting product images should communicate from product fields and review pain points; it does not generate image files, run ads, or publish listings, and it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill with an AI agent to inspect product fields and review issues, quote any paid ARI operation, and produce a text plan for what the main and supporting product images should communicate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The command-line tool can run paid remote ARI operations that may be broader than a strict image-planning-only expectation.

Mitigation: Keep use limited to the documented listing/images workflow, require quote review and explicit confirmation before any run, and do not allow custom workflow or focus values.

Risk: The skill saves or uses an ARI API key and sends Amazon product, review, and account-related requests to ari.funewa.com.

Mitigation: Install only in trusted environments, avoid sharing account context unnecessarily, and revoke the key or remove ~/.ari/config.json when use stops.

Risk: Unexpected custom workflow or focus values could broaden product-operation behavior.

Mitigation: Use the artifact whitelist and fixed contract of listing/images with the ops_listing output template.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/image-planner)
- [Amazon product image planning operation workflow](artifact/references/operation-workflow.md)
- [Amazon product image planning API reference](artifact/references/reference.md)
- [ARI API and authorization endpoint](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise prose and inline bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local ARI API key configuration; paid operations require a quote and explicit user confirmation before execution.]

## Skill Version(s):

1.4.11 (source: server release metadata, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
