## Description: <br>
Context7 MCP provides intelligent documentation search and context retrieval for libraries through the Context7 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to search for library documentation, retrieve relevant documentation context, and apply Context7 best practices when answering implementation questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation search terms and questions are sent to Context7. <br>
Mitigation: Avoid including credentials, proprietary code, private URLs, customer data, or other sensitive material in queries. <br>
Risk: The skill requires a Context7 API key that may be stored in an environment variable or local .env file. <br>
Mitigation: Use a dedicated API key, keep .env files out of source control and logs, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [Context7 API documentation](https://context7.com/docs) <br>
- [Context7 documentation index](https://context7.com/docs/llms.txt) <br>
- [Context7 dashboard](https://context7.com/dashboard) <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/context7) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI output and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node/npm and a CONTEXT7_API_KEY for live Context7 API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
