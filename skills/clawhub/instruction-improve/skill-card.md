## Description:

Analyzes Amazon review questions about installation, use, and maintenance to identify instruction-improvement priorities and supporting evidence; requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to turn Amazon review questions and complaints into evidence-backed recommendations for improving product instructions and related customer guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI workflows can spend credits, and some account rules may allow small paid operations without an additional prompt.

Mitigation: Use explicit quote-only wording when checking prices, disable or lower auto-confirm rules when needed, and review credit costs before allowing paid analysis or collection.

Risk: The skill can affect ongoing account behavior through monitoring, schedules, exports, or account confirmation settings.

Mitigation: Review each monitoring, schedule, export, or account-setting change before allowing it, and require clear user intent for persistent changes.

Risk: The skill requires access to an ARI account and an ARI API key.

Mitigation: Use the browser authorization flow or local environment configuration, avoid sharing keys in chat, and install only when account-level ARI access is acceptable.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/instruction-improve)
- [ARI Amazon Review Assistant User Guide](使用说明.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing and Plans](https://ari.funewa.com/zh/billing)
- [ARI Product Management](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis and recommendations, with occasional inline shell commands or configuration steps for setup and troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include review evidence, trend caveats, report links, credit usage, and ARI account or authorization status when relevant.]

## Skill Version(s):

1.4.8 (source: server release evidence, skill frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
