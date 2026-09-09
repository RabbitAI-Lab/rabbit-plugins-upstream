## Description:

Checks an Amazon listing's information completeness, review evidence, and common misunderstanding risks for listing health diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to assess a specified ASIN's listing health, identify review-backed issues, and prioritize evidence-supported improvements. It is scoped to listing health diagnosis, not full listing copywriting, advertising, inventory, orders, or profit analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits, and some account rules may allow small paid analyses to run without a fresh prompt.

Mitigation: Use "only quote, don't execute" for price checks, set autoconfirm off when every charge should be confirmed, and execute paid runs only after clear user consent when confirmation is required.

Risk: The skill handles an ARI API key and Amazon review or listing data.

Mitigation: Use it only if ARI is trusted with that key and data, keep keys out of chat and reports, and rebuild or rotate keys when authentication problems occur.

Risk: The skill can change ongoing monitoring or confirmation settings beyond a one-time health check.

Mitigation: Treat schedule, watch, and autoconfirm changes as explicit account actions; state the setting and cost impact before making changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/listing-health)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [Operation Workflow](references/operation-workflow.md)
- [API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with concise listing-health analysis, review evidence, operational guidance, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations may consume ARI credits under server confirmation rules.]

## Skill Version(s):

1.4.8 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
