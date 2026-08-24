## Description:

Guides agents through Amazon listing optimization using Pangolinfo tools to analyze competitor listings, customer review themes, search terms, category fit, and IP-risk signals before drafting copy for Seller Central.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and marketplace consultants use this skill to rewrite Amazon listings from competitor PDP data, VOC from reviews, backend search-term constraints, category context, and preliminary IP checks. It produces copy and analysis intended for review before publication in Seller Central.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill instructs the agent to access PANGOLINFO_API_KEY, which could expose credentials if mishandled.

Mitigation: Use MCP or environment configuration for credentials, avoid printing or summarizing secrets in chat, and review credential-handling instructions before installation.

Risk: Generated listing copy and IP-risk checks can be incomplete or misleading if source data is missing, stale, or only preliminary.

Mitigation: Review generated copy, source references, and IP-risk findings before publishing listings or making inventory decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-listing-optimization)
- [Pangolinfo](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, API Calls, Guidance]

**Output Format:** [Markdown report with listing copy, tables, tool-call guidance, and concise risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Amazon title drafts, five bullet points, backend search terms, VOC summaries, category checks, and preliminary IP-risk recommendations.]

## Skill Version(s):

4.0.0 (source: server release metadata; artifact frontmatter lists 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
