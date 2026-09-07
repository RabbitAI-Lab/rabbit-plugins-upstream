## Description:

Dissects user-provided or authorized competitor Amazon product pages, including titles, bullets, images, and review evidence, to identify reusable structure and risks without claiming true bestseller status, sales, inventory, ads, orders, or return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators use this skill to compare a main ASIN with authorized competitor product pages and generate a structured teardown of listing content, review evidence, and operational risks. It is intended for static product-page analysis after ARI account authorization and quote confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can use the user's ARI account for billing, monitoring, export, credential handling, and analysis operations beyond a static teardown.

Mitigation: Install only if the ARI service is trusted, keep per-charge confirmation enabled when cost control is needed, and review quoted costs before approving paid runs.

Risk: Custom ARI endpoint environment variables could redirect credential-bearing requests if deliberately enabled.

Mitigation: Avoid ARI_BASE_URL and ARI_ALLOW_CUSTOM_BASE unless operating and trusting the target endpoint.

Risk: Monitoring, schedule changes, and exports can affect future costs or local files.

Mitigation: Review monitoring or schedule changes before agreeing, and choose export paths that will not overwrite important files.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Dedicated Operation Workflow](references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bestseller-teardown)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text, with shell commands or JSON snippets only when setup, troubleshooting, or advanced use requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include data scope, evidence-backed findings, limitations, quoted cost or credits used when applicable, and report links when returned by ARI.]

## Skill Version(s):

1.4.7 (source: server release metadata, skill frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
