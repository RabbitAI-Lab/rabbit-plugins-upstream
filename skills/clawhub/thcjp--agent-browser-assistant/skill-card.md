## Description:

浏览器代理助手 helps agents automate browser interactions, collect web data, wrap API calls, and return directly usable results for Chinese-language workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and automation users can use this skill when they intentionally need browser task automation, page data collection, or API request and response handling inside an agent workflow. It is not suited for decisions that require deterministic or independently verified results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill as suspicious because it requests broad local command and file authority with vague activation rules.

Mitigation: Review the skill before installing and grant only the minimum read, write, and command permissions needed for a bounded task.

Risk: Browser automation and data collection can involve credentials, proxies, or scraping tasks that create elevated operational and compliance risk.

Mitigation: Avoid granting credentials, proxy access, or scraping authority unless target sites, rate limits, data handling, and allowed actions are explicitly scoped.

Risk: The artifact describes dynamic page interaction, retries, custom scripts, and data parsing that may produce incomplete or incorrect results when page structure or network behavior changes.

Mitigation: Validate extracted data against the source, set timeout and retry limits, and require human review before using results in consequential workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-browser-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured text, with JSON examples and shell command snippets when configuration is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe browser actions, API request handling, extracted data, error states, and setup guidance.]

## Skill Version(s):

1.0.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
