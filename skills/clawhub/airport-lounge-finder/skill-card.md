## Description:

全球50+机场贵宾厅查询，支持按机场/信用卡权益/准入方式三维度搜索，覆盖PP卡/龙腾出行/航司休息室，零配置即装即用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and agents use this skill to look up airport lounge options by airport, credit-card benefit, or lounge access method. It returns location, access conditions, facilities, ratings, and related informational guidance from a bundled local dataset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Airport lounge access rules, credit-card benefits, locations, and facility details may be outdated or incomplete.

Mitigation: Treat results as informational and verify current access rules with the airport, airline, bank, or lounge provider before relying on them.

Risk: The bundled data and user-facing output are primarily Chinese-language, which may limit usability for some users.

Mitigation: Use the skill where Chinese-language lookup output is acceptable, or review and adapt responses for the intended audience before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/airport-lounge-finder)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown lookup results with JSON status messages for errors or empty results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a locally bundled Chinese-language reference dataset and does not require network access.]

## Skill Version(s):

1.0.9 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
