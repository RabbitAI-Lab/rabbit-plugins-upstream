## Description:

Combines Amazon product details and review evidence to diagnose mobile Listing reading order, information density, and comprehension blockers without handling ads, inventory, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace operators use this skill to review how a product Listing reads on mobile, using product details and review evidence to prioritize clearer messaging and action items. It is intended for Listing expression diagnostics, not for ad bidding, stock or order analysis, or automatic page publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account features, saved API-key credentials, paid analysis workflows, and persistent account settings.

Mitigation: Install only for users comfortable with that account authority; configure ARI to ask before paid actions when appropriate and use "只报价，不执行" for pricing-only requests.

Risk: Paid operations may deduct credits, and some account rules can allow small paid analyses to run without an immediate confirmation prompt.

Mitigation: Review quotes, balances, and auto-confirm rules before execution; require explicit confirmation for operations runs and account-level changes unless the user has already configured a threshold.

Risk: Network interruption during a confirmed paid workflow may leave a report running or already charged.

Mitigation: Check the existing report or operation status by report ID, ASIN, or request ID before rerunning a confirmed paid command.

Risk: Monitoring, competitor bindings, exports, workbench status, and auto-confirm settings can persist beyond a single analysis.

Mitigation: Treat these as account management actions and perform them only after the user clearly requests the specific change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/mobile-listing)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [Mobile Listing Operation Workflow](artifact/references/operation-workflow.md)
- [ARI Amazon Review Assistant User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text reports, with JSON summaries and shell command snippets when needed for setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN/site scope, review sample limits, report IDs, report links, credit usage, and account status when returned by ARI.]

## Skill Version(s):

1.4.7 (source: evidence release metadata, SKILL.md frontmatter, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
