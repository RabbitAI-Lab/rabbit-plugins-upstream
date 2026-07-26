## Description: <br>
Api Doc Writer helps developers draft REST API documentation with endpoint descriptions, request and response formats, authentication notes, status code guidance, security recommendations, and change records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and API teams use this skill to create consistent REST API documentation, including interface overviews, authentication conventions, request and response examples, error handling, security recommendations, and multi-module document structure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated API examples or documentation may include sensitive internal endpoints, tokens, or customer data. <br>
Mitigation: Use sanitized examples by default, omit real secrets, and review generated documentation before sharing or committing it. <br>
Risk: The optional callback_url parameter may send result data to an unintended endpoint. <br>
Mitigation: Use callback_url only with trusted HTTPS endpoints after confirming what data will be transmitted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/api-doc-writer) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown API documentation with JSON, HTTP, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include template sections, endpoint tables, example payloads, error-handling notes, and security recommendations.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
