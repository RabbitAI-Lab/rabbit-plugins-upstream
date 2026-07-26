## Description: <br>
Agent Browser Stagehand helps agents automate browser navigation, page interaction, and content extraction through natural-language CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to direct browser automation tasks such as navigation, clicking, text entry, extraction, screenshots, and structured result capture without hand-writing selectors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can interact with third-party sites, and the security summary flags broad scope plus anti-bot bypass guidance. <br>
Mitigation: Use only for authorized sites and supervised tasks; avoid bypassing access controls, anti-bot protections, site terms, or pages containing sensitive personal or account data. <br>
Risk: Natural-language browser actions may click, enter text, or extract content differently than intended when pages change or instructions are underspecified. <br>
Mitigation: Review planned actions and outputs before relying on results, keep retries bounded, and require user confirmation for sensitive or irreversible site interactions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/agent-browser-stagehand) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result structures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return structured execution logs, extracted page data, status fields, timing metadata, and screenshots when supported by the host agent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
