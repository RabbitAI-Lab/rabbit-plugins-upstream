## Description:

零售连锁拓店选址专家，分析品牌门店规模、区域层级、业态结构、周边画像与候选点竞争。适用于拓展经理、选址团队和区域负责人筛选机会城市、比较地址或判断覆盖空白。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External retail expansion managers, site-selection teams, and regional leaders use this skill to assess published retail brand coverage, compare opportunity areas or candidate sites, and identify items for field verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand queries, candidate coordinates, and public store IDs may be sent to the external DDT retail API.

Mitigation: Install and use this skill only when that provider is intended, and avoid submitting confidential expansion plans or sensitive location data unless approved.

Risk: DDT_API_KEY exposure could give unauthorized access to the API.

Mitigation: Keep DDT_API_KEY in a controlled environment variable and do not place real keys in chat, logs, source control, or skill files.

Risk: Retail coverage, preview truncation, or missing fields could lead to overconfident site-selection conclusions.

Mitigation: Check coverage and preview.truncated indicators, label unavailable coverage explicitly, and treat nearby or site-screen results as initial screening rather than a complete market list.

## Reference(s):

- [DDT retail API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-retail-expansion-expert)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with concise findings, key metrics, coverage notes, and occasional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the current published retail snapshot returned by the DDT retail API and limits detailed store output to user-requested public previews.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
