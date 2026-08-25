## Description:

Query TikTok Shop e-commerce analytics through the bundled Python `kalo` CLI for product, shop, creator, video, livestream, and category rankings, details, and revenue trends from KaloData.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maosen-sgy](https://clawhub.ai/user/maosen-sgy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce operators use this skill to retrieve and compare TikTok Shop market, product, shop, creator, video, livestream, and category metrics for sourcing research, creator scouting, and performance diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KaloData queries may consume paid API credits, especially when playbooks fan out into multiple ranking and detail calls.

Mitigation: Check remaining quota with `kalo credit`, mention expected credit spend before high-volume analysis, and batch detail lookups instead of issuing unnecessary repeated calls.

Risk: Creator detail results may include personal contact information.

Mitigation: Retrieve and share only the contact fields needed for a legitimate outreach or analysis purpose.

Risk: TikTok Shop analysis can be misleading when conclusions are drawn without same-category, same-price-band, or same-follower-tier benchmarks.

Mitigation: Follow the bundled playbooks, state the comparison basis for each metric, and avoid claims that the KaloData API does not support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maosen-sgy/skills/kalodata)
- [Analysis playbooks](references/playbooks.md)
- [KaloData Open Center account](https://www.kalodata.com/open-center/account)
- [KaloData pricing](https://www.kalodata.com/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline shell commands; CLI output may be TOON or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided KaloData API key and may return TikTok Shop metrics, revenue trends, and creator contact fields from authorized API calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
