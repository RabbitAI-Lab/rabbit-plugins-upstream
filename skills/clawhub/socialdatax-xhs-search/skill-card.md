## Description: <br>
Searches Xiaohongshu/XHS/RedNote notes through SocialDataX for keyword research, content planning, competitor analysis, market observation, and trend scanning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and content researchers use this skill to run SocialDataX-backed Xiaohongshu/XHS searches and summarize visible note evidence for topic discovery, content planning, competitor research, and trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to SocialDataX as third-party API calls. <br>
Mitigation: Use the skill only for SocialDataX-backed Xiaohongshu/XHS research, avoid sensitive search terms, and clarify intent when a request is generic research rather than XHS/RedNote-focused. <br>
Risk: The skill depends on SOCIALDATAX_API_KEY at runtime. <br>
Mitigation: Keep the key in the environment, do not embed it in generated files or outputs, and confirm the configured account when balance or credit errors occur. <br>
Risk: Fetched pages may not represent complete platform coverage. <br>
Mitigation: State the query bounds in summaries, use explicit page or recent-day windows when relevant, and separate visible evidence from interpretation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search) <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>
- [Publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with CLI examples, parameter guidance, and summarized search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Xiaohongshu/XHS search using SOCIALDATAX_API_KEY; results may include note URLs and IDs that must be preserved exactly.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
