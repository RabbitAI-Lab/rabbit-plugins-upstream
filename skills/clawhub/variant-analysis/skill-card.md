## Description:

Analyzes Amazon review data across color, size, and specification variants to identify weak and strong variants, explain review drivers, and support ARI reports, monitoring, competitor comparison, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and analysts use this skill to compare parent-child ASIN variant performance, find color, size, or specification variants that drag down ratings, and turn ARI review data into concise operational guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run paid ARI workflows that may spend credits automatically when account rules allow it.

Mitigation: Use quote-only requests when unsure, set the skill to ask before every paid operation, and confirm costs before paid analysis, collection, leaderboard, or advise workflows.

Risk: The skill can change future spending-confirmation behavior and manage schedules, watches, competitor bindings, exports, and workbench status from chat.

Mitigation: Review requested confirmation, monitoring, export, competitor, and workbench changes before allowing the agent to run them.

Risk: The skill requires ARI account authorization and uses an ARI API key.

Mitigation: Authorize through the documented browser flow or a local environment variable, and do not paste credentials into reports or chat transcripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/variant-analysis)
- [ARI CLI and API Reference](references/reference.md)
- [ARI User Guide](使用说明.md)
- [ARI Account and Authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and concise text summaries, with shell commands or configuration steps when setup, troubleshooting, export, or workflow execution requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, CSV or Markdown/HTML export references, data scope notes, credit usage, and account confirmation status when returned by ARI.]

## Skill Version(s):

1.4.13 (source: frontmatter, _meta.json, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
