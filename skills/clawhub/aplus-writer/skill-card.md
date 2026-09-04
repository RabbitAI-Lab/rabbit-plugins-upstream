## Description:

Uses Amazon product details and review evidence to plan A+ content modules, information hierarchy, and buyer-question responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to plan Amazon A+ content modules, messaging priorities, and responses to buyer concerns from product and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill exposes broader ARI review, monitoring, export, and paid-operations capabilities than its A+ content-planning description suggests.

Mitigation: Review before installing if only A+ planning is needed, and install only when those broader ARI capabilities are acceptable.

Risk: The skill can use an ARI API key with access to credits, saved reports, exports, monitoring settings, and account-side workflow state.

Mitigation: Keep the API key out of reports and command examples, use the documented setup or environment-variable flow, and rotate the key if the workspace is shared or compromised.

Risk: Paid ARI operations can consume account credits, and interrupted paid commands may already have produced a charged report.

Mitigation: Keep autoconfirm limits conservative, preserve quote-before-confirm flows, and check existing reports or operation status before retrying interrupted paid commands.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Amazon A+ Operation Workflow](references/operation-workflow.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with ARI-backed report summaries and inline command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN, site, sample size, report ID, credits used, account balance, and report URL when returned by ARI.]

## Skill Version(s):

1.4.5 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
