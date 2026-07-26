## Description: <br>
Searches Xiaohongshu PGY for bloggers, guides browser-based login and search, extracts blogger profile, audience, content, and pricing data, and compiles structured reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, and business-development teams use this skill to research Xiaohongshu PGY bloggers by keyword or region and turn extracted profile, audience, content, and pricing data into structured Markdown reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to handle PGY account credentials and login flows. <br>
Mitigation: Use only accounts the user is authorized to automate, avoid sharing credentials in plain chat where possible, and require user confirmation before login. <br>
Risk: The skill collects platform analytics, pricing, and audience-demographic data that may be sensitive business information. <br>
Mitigation: Limit collection to the user's stated scope and share generated reports only with authorized recipients. <br>
Risk: Browser automation could collect more data than intended if the search scope is unclear. <br>
Mitigation: Confirm each data-collection run, including keywords, regions, and target bloggers, before extracting profile details. <br>


## Reference(s): <br>
- [PGY Operation Guide](references/pgy-operation-guide.md) <br>
- [Xiaohongshu PGY Platform](https://pgy.xiaohongshu.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/zhaobod1/skills/huo15-xhs-pgy-test) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown reports with tables, browser automation snippets, and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-authorized PGY account and can include sensitive pricing and audience-demographic data.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
