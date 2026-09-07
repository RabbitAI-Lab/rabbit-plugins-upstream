## Description:

Weather information lookup tool covering Chinese cities and counties for current weather, forecasts, and weather alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencentnewsteam](https://clawhub.ai/user/tencentnewsteam)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Tencent weather data for Chinese city and county-level administrative regions. It checks CLI and API-key readiness, then guides or runs weather CLI commands for current conditions, forecasts, alerts, and related returned sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation or update of a local Tencent News CLI from remote installer scripts.

Mitigation: Review and verify installer sources before installation; prefer downloading and verifying installers manually instead of piping remote scripts directly into a shell.

Risk: The skill executes local CLI commands to retrieve weather data and inspect CLI state.

Mitigation: Review commands before running them, use the bundled wrapper scripts, and stop on CLI errors rather than substituting another data source.

Risk: The skill requires API-key configuration for the Tencent News CLI.

Mitigation: Enter API keys locally only, do not share real keys with the agent, and rotate or clear keys if exposure is suspected.

## Reference(s):

- [tencent-weather ClawHub skill page](https://clawhub.ai/tencentnewsteam/skills/tencent-weather)
- [TencentNewsTeam publisher profile](https://clawhub.ai/user/tencentnewsteam)
- [Manual installation guide](references/installation-guide.md)
- [Manual update guide](references/update-guide.md)
- [API key setup guide](references/env-setup-guide.md)
- [Tencent News API key page](https://news.qq.com/exchange?scene=appkey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, often preserving the CLI's returned weather sections; may include shell commands for setup and troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are limited to CLI-returned weather data or directly mapped fields; API keys are user-provided locally and should not be collected or echoed.]

## Skill Version(s):

1.0.5 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
