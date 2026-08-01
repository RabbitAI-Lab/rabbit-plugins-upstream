## Description: <br>
Connect OpenClaw or another MCP-compatible agent to Google Search Console to retrieve read-only property, performance, sitemap, and URL inspection data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2winter-dev](https://clawhub.ai/user/2winter-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and SEO analysts use this skill to connect an agent to an authorized Google Search Console account, select a property, and generate read-only performance, sitemap, and URL inspection reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects to a third-party remote MCP service that requests read-only Google Search Console OAuth access. <br>
Mitigation: Verify the OAuth consent screen and scopes, never paste passwords or tokens into configuration, and revoke the OAuth grant or remove the MCP server when access is no longer needed. <br>
Risk: Search Console results can be limited, delayed, or scoped to selected properties, date ranges, filters, and top rows. <br>
Mitigation: Report the exact property, date range, search type, filters, dataState, and uncertainty before making SEO recommendations. <br>


## Reference(s): <br>
- [GSC Connect product guide](https://yusihk.com/en/gsc-connect-codex-plugin-google-search-console/) <br>
- [GSC Connect English documentation](https://gsc.yusihk.com/docs) <br>
- [GSC Connect Traditional Chinese documentation](https://gsc.yusihk.com/zh-hant/docs) <br>
- [ClawHub skill page](https://clawhub.ai/2winter-dev/skills/gsc-connect) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured report sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Google Search Console observations with property, date range, filters, data limitations, and prioritized checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
