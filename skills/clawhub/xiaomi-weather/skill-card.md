## Description:

中国天气查询（小米天气 App 同款数据源）。支持城市名/城市代码，实时天气、多日预报、空气质量、降水概率、日出日落。数据与小米天气 App 完全一致，比 wttr.in 更适合国内使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query current weather, multi-day forecasts, air quality, precipitation probability, and sunrise or sunset details for Chinese cities from Xiaomi Weather data. It supports built-in common city names, nine-digit city codes, and JSON output for scripted workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends weather lookup queries to Xiaomi's weather API and may download a fallback city list from GitHub.

Mitigation: Install only when that disclosed network behavior is acceptable for the intended environment.

Risk: The fallback city list is cached in a low-risk temporary file.

Mitigation: Harden the cache path to a per-user directory with restrictive permissions before deployment in stricter environments.

## Reference(s):

- [Xiaomi Weather API documentation](https://github.com/huanghui0906/API/blob/master/XiaomiWeather.md)
- [Common city code table](references/cities.tsv)
- [Full Xiaomi weather city database](https://github.com/huanghui0906/API/blob/master/xiaomi_weather.db)
- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/xiaomi-weather)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Terminal text output or raw JSON from a shell command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network access is required for Xiaomi weather queries and for fallback city lookup when a city is not built in.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
