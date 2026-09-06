## Description:

腾讯天气预警/异常天气查询工具，覆盖雨雪、雾霾、空气质量、寒潮、高温和台风等预警；当用户查询某地天气预警或最近有什么异常天气时使用，仅做一次性查询并返回结果，不提供订阅或主动推送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencentnewsteam](https://clawhub.ai/user/tencentnewsteam)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask an agent for current Tencent weather alerts or abnormal weather affecting Chinese locations. The skill checks local CLI readiness, dynamically discovers the Tencent News CLI weather capability, runs a one-time lookup, and returns only the alert details present in the CLI result.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill depends on installing or updating tencent-news-cli through Tencent remote installer scripts.

Mitigation: Review the installer source and CLI origin before installation; prefer signed or checksum-verified installers where available.

Risk: The agent may run a broad external CLI on the user's machine.

Mitigation: Constrain use to the bundled wrappers and the weather/API-key commands needed for the current request; stop on CLI failures instead of trying alternate tools.

Risk: Weather lookup requires a Tencent News API key stored locally.

Mitigation: Configure the key directly in the terminal and do not paste, request, echo, or log the real key in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencentnewsteam/skills/tencent-weather-alert)
- [API Key configuration guide](references/env-setup-guide.md)
- [Manual installation guide](references/installation-guide.md)
- [Manual update guide](references/update-guide.md)
- [Tencent News API Key page](https://news.qq.com/exchange?scene=appkey)
- [Tencent News CLI macOS/Linux installer](https://mat1.gtimg.com/qqcdn/qqnews/cli/hub/tencent-news/setup.sh)
- [Tencent News CLI Windows installer](https://mat1.gtimg.com/qqcdn/qqnews/cli/hub/tencent-news/setup.ps1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text, with inline shell commands for setup and troubleshooting when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weather results are one-time responses from Tencent CLI output; setup guidance avoids collecting or echoing real API keys.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
