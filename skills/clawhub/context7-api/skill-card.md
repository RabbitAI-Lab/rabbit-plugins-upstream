## Description: <br>
Fetches up-to-date library documentation through the Context7 API for library search, API usage, implementation guidance, and debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding agents use this skill to search for libraries and fetch current documentation context before implementing, debugging, or reviewing features that depend on third-party packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the skill embeds and uses a fallback Context7 API key when CONTEXT7_API_KEY is not configured. <br>
Mitigation: Require users to configure their own CONTEXT7_API_KEY and prefer a release that removes the embedded fallback key before commercial deployment. <br>
Risk: Library names, library IDs, and documentation queries are sent to the external Context7 API. <br>
Mitigation: Avoid sending confidential project details in queries and document the external request behavior for users before installation. <br>


## Reference(s): <br>
- [Context7 API endpoint](https://context7.com/api/v2) <br>
- [ClawHub skill page](https://clawhub.ai/am-will/skills/context7-api) <br>
- [Publisher profile](https://clawhub.ai/user/am-will) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON from the Context7 API, often used as Markdown-ready documentation context.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports library search, documentation context queries, output type selection, and optional token limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
