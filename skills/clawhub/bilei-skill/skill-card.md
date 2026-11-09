## Description:

A shopping-advice agent that checks product risks and evidence quality, compares options against a budget, and gives recommendations bounded by the available evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

Consumers in China use this agent to check safety and reliability concerns before buying, compare suitable products against a budget, and receive an evidence-based recommendation with uncertainties made clear.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The installation example uses an unpinned skill source.

Mitigation: Review the source and choose a specific release or commit before installing.

Risk: Shopping comparisons may include unsupported explanations about product branding, and scanner coverage was partial.

Mitigation: Check consequential claims against current authoritative or independent sources, label uncertain details, and review the bundled references.

## Reference(s):

- [Evidence grading and source credibility guide](references/source-credibility.md)
- [Source repository](https://github.com/zhashushu/bilei-skill)
- [ClawHub skill page](https://clawhub.ai/zhashushu/skills/bilei-skill)
- [CCTV News report on AI-generated shopping misinformation](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=12967278106578155767)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown shopping assessment with evidence-graded findings, product comparisons, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are limited by cited evidence; prices and availability can change.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
