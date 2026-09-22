## Description:

基于飞常准数据，提供航班实时动态、延误分析、舒适度评分、机场天气查询，覆盖全球航班，零配置即用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-assistant agents use this skill to check live flight status, route-level delays, comfort scoring, and airport weather using VariFlight data. It is designed for Chinese-language flight-tracking workflows with flight numbers, city names, airport names, or airport codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight, route, date, and airport-weather queries are sent through a fixed Tencent SCF proxy to access VariFlight data.

Mitigation: Use a narrowly scoped PROXY_TOKEN and avoid entering travel details that users consider highly sensitive.

Risk: Live flight and weather data can be delayed, incomplete, or changed by airlines and airports after the skill responds.

Mitigation: Verify critical itinerary decisions with the airline, airport, or official travel provider before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/variflight-tracker)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [VariFlight proxy endpoint](https://1439498936-eqcpuaevzz.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API Calls, guidance]

**Output Format:** [Markdown status summaries and JSON error messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include flight-status tables, route summaries, comfort scores, airport-weather tables, and flight-impact assessments.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
