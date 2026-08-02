## Description: <br>
Connects an AI agent to Skilder's remote MCP endpoint and starts the OAuth connection flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skilder](https://clawhub.ai/user/skilder) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure a supported agent host to connect to Skilder over MCP, complete OAuth, and inspect the roles and skills the server exposes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs the agent to make persistent MCP configuration changes. <br>
Mitigation: Confirm the exact MCP host and configuration file before applying changes, and prefer a reversible or temporary setup. <br>
Risk: The skill directs the agent to start OAuth and connect to the remote MCP server without asking first. <br>
Mitigation: Review Skilder's OAuth permissions and exposed tools before approving the browser sign-in. <br>


## Reference(s): <br>
- [ClawHub listing for connect-to-skilder](https://clawhub.ai/skilder/skills/connect-to-skilder) <br>
- [Skilder skills homepage](https://github.com/skilder-ai/skills) <br>
- [Skilder remote MCP endpoint](https://app.skilder.ai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with CLI commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist MCP configuration and initiate an OAuth browser sign-in.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
