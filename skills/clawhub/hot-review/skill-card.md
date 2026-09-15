## Description:

hot-review helps Amazon sellers analyze collected product reviews to identify buyer needs, positive selling points, negative-review risks, trends, competitor gaps, and listing or product improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators, product researchers, and listing teams use this skill to turn ARI-collected Amazon review data into concise VOC reports, competitor comparisons, trend summaries, keyword insights, and listing or product-improvement recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send Amazon review data and account requests to ari.funewa.com.

Mitigation: Install only if connecting an ARI account and sending review data to the ARI service is acceptable.

Risk: Some analysis flows may spend ARI account credits automatically under service auto-confirm rules.

Mitigation: Before paid analysis, ask the agent to only quote without executing or to ask before every credit deduction.

Risk: Generated review insights may be incomplete when ARI has limited sample coverage, short time windows, or incomplete variant data.

Mitigation: Require the agent to state sample scope, collection window, and data gaps, and verify important product decisions with additional evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/hot-review)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI API reference](artifact/references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI report center](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and reports, concise text guidance, and shell commands for the bundled ARI CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, sample-scope notes, credit usage, CSV or Markdown/HTML export guidance, and API-derived review evidence when available.]

## Skill Version(s):

1.4.11 (source: server release evidence, SKILL.md frontmatter, _meta.json, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
