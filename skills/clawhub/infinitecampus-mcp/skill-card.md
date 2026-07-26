## Description: <br>
Provides an MCP server for Infinite Campus Campus Parent so an agent can read student grades, attendance, assignments, messages, documents, and related school account information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to configure and interact with a user's own Infinite Campus Campus Parent account. It supports retrieving student records, documents, and school messages, and can help send school messages when the user has authorized that action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive student records, including grades, attendance, behavior, fees, food service, documents, and messages. <br>
Mitigation: Install it only for an account you are authorized to use, protect credentials and session access, and require explicit confirmation before retrieving sensitive categories. <br>
Risk: The skill can send school messages from the configured parent account. <br>
Mitigation: Require explicit user confirmation before sending any message, and review the recipient, subject, and body before submission. <br>
Risk: The browser-cookie fallback can reuse an existing portal session. <br>
Mitigation: Disable the fallback with IC_DISABLE_FETCHPROXY=1 when session reuse is not intended, and keep browser sessions and local credentials private. <br>


## Reference(s): <br>
- [npm package](https://www.npmjs.com/package/infinitecampus-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP configuration guidance and tool-mediated access to sensitive student records, documents, messages, and school account data.] <br>

## Skill Version(s): <br>
2.3.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
