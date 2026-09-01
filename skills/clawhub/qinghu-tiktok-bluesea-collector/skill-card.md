## Description:

Helps agents identify emerging TikTok Shop products, verify product details, find matching 1688 suppliers, and estimate margins using Qinghu data APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and sourcing teams use this skill to discover rising TikTok Shop products, compare supplier options on 1688, and produce prioritized product shortlists with margin assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token and may spend credits during product and supplier data calls.

Mitigation: Require user approval before the first credit-consuming call, read tokens only from the user or configured environment variables, and report actual usage from returned cost metadata.

Risk: Large product or supplier result sets may create local exported data files.

Mitigation: Tell users when files are created and keep exported data scoped to the requested TikTok/1688 research workflow.

Risk: Margin and supplier recommendations can be wrong if assumptions or supplier quality are not verified.

Mitigation: Label marketplace, period, sample size, freight, and commission assumptions, and advise users to confirm supplier details and samples before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-bluesea-collector)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries with optional exported data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product candidate lists, supplier matches, margin estimates, priority rankings, and concise assumptions for the data period and marketplace.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
