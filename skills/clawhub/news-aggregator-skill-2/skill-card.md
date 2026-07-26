## Description: <br>
Comprehensive news aggregator that fetches, filters, and deeply analyzes real-time content from 8 major sources: Hacker News, GitHub Trending, Product Hunt, 36Kr, Tencent News, WallStreetCN, V2EX, and Weibo. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tonyliu9189](https://clawhub.ai/user/tonyliu9189) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch multi-source news, perform broad or keyword-targeted scans, and generate concise Chinese newsletter-style briefings with links, metadata, and interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts public news sources and may deep-fetch article text from external sites. <br>
Mitigation: Install only if this network access is acceptable for the intended environment, and review fetched content before relying on it. <br>
Risk: Generated briefings are saved locally in the reports/ directory by default. <br>
Mitigation: Review saved reports for sensitive prompts, proprietary topics, or unwanted retained content before sharing or keeping them. <br>
Risk: The submitted artifact references helper script and template files that are not included. <br>
Mitigation: Verify the actual implementation files available in the runtime environment before using the skill for production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tonyliu9189/skills/news-aggregator-skill-2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown newsletter-style reports with source links, metadata, analysis bullets, and optional saved report files; helper fetches return JSON when available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are expected to be written in Simplified Chinese and saved under reports/ with timestamped filenames.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
