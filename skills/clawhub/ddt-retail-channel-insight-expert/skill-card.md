## Description:

Analyzes retail chain store networks, category structure, regional coverage, and brand comparisons for convenience stores, supermarkets, pharmacies, beauty retailers, and similar brands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Market, channel, and competitive-intelligence teams use this skill to evaluate retail brand scale, store formats, city rankings, regional concentration, surroundings, and competitive coverage using the gotoshop-ai retail data API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if users paste DDT_API_KEY into chat, logs, or version control.

Mitigation: Keep DDT_API_KEY in a local or controlled runtime environment and never include real keys in skill text, conversations, logs, or repositories.

Risk: Retail brand, coordinate, or public store-ID queries are sent to the gotoshop-ai retail data API when users request those analyses.

Mitigation: Install and use the skill only when that API use is intended, and verify DDT_OPEN_BASE before making requests.

Risk: Store snapshots, coverage gaps, or truncated previews can lead to overstated market conclusions.

Mitigation: Base conclusions only on API responses, report coverage and data version, narrow truncated queries, and mark unavailable coverage explicitly instead of inferring missing values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-retail-channel-insight-expert)
- [DDT retail API homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with concise analytical prose and optional bash or curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should report conclusions, three to six key metrics, coverage and data version, any explicitly requested limited store details, and uncovered items.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
