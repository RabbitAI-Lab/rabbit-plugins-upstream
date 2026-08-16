## Description:

Helps monitor competitor product patent infringement risk by using the user's company name plus either uploaded competitor product files or a competitor company name to retrieve the user's patent portfolio, extract product technical features, compare claim elements, and produce a risk-rated infringement analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent, product, and legal-operations teams use this skill to screen whether competitor products may read on the user's active patent portfolio and to prioritize follow-up review. The output is preliminary business research and is not a substitute for review by a qualified patent professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated infringement conclusions may be incomplete or legally incorrect because the skill provides preliminary patent-risk analysis.

Mitigation: Have a qualified patent professional review high-risk findings before using them for litigation, enforcement, or business action.

Risk: The workflow may analyze uploaded competitor product documents and public web sources through a connected PatSnap MCP account.

Mitigation: Install and use the skill only in environments approved for those documents and connected account permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-infringement-watch)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown infringement analysis report with summary, patent portfolio table, product feature list, claim comparison matrix, equivalence analysis, risk ratings, and recommended actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured patent, web search, web fetch, and file parsing tools to produce evidence-backed results; without the required MCP configuration it can only provide an analysis framework.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
