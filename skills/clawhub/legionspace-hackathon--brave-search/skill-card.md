## Description: <br>
Headless web search and page-content extraction using Brave Search, with optional Markdown extraction from result pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search documentation, facts, current web content, and API references without an interactive browser. It can also fetch a specific URL and return readable page content as Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and fetched URLs are sent to external websites. <br>
Mitigation: Do not submit secrets, private internal URLs, confidential project names, or sensitive personal data through this skill. <br>
Risk: Operators may expect BRAVE_API_KEY to control network access, but the security guidance says the current implementation does not use it. <br>
Mitigation: Verify the runtime behavior before deployment and do not rely on BRAVE_API_KEY for access control, quota tracking, or audit expectations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/brave-search) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Plain text search results with optional Markdown page content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include title, link, snippet, and optional extracted page content; embedded page content is truncated by the implementation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and package.json; artifact _meta.json reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
