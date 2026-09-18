## Description:

Get current weather, air quality, and 3-day forecasts for China using Moji Weather, including temperature, humidity, wind, and lifestyle tips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create curl-based weather queries for Chinese province, city, and district locations and interpret current conditions, air quality, short forecasts, and lifestyle tips. It is useful when an agent needs weather guidance without API-key setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weather queries send the requested location to external weather services.

Mitigation: Use only locations the user has agreed to share, prefer coarse locations when precise districts are unnecessary, and avoid sending sensitive contextual details.

Risk: External weather services may be unavailable or return stale or inaccurate conditions.

Mitigation: Treat results as informational, retry or compare sources when availability matters, and avoid relying on the output for safety-critical decisions.

## Reference(s):

- [Moji Weather](https://tianqi.moji.com)
- [MSN Weather](https://www.msn.cn/zh-cn/weather/)
- [Open-Meteo API documentation](https://open-meteo.com/en/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and weather summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include outbound weather requests containing the queried location.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
