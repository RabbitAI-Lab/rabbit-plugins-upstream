## Description: <br>
Query and analyze Claude Code session data from a remote server, including conversation history, tool calls, tasks, prompt search, and usage statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myakove](https://clawhub.ai/user/myakove) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Claude Code session records from a configured ccsinfo server, including recent sessions, messages, tool calls, tasks, project activity, and usage statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A ccsinfo server can expose private Claude Code session history over the network. <br>
Mitigation: Use only with a ccsinfo server you control, bind it to 127.0.0.1 or a private VPN when possible, and add firewall or authentication controls if available. <br>
Risk: Retrieved session data may include prompts, outputs, tool results, code, secrets, and old instructions. <br>
Mitigation: Treat all retrieved session data as sensitive and avoid plain HTTP on shared networks. <br>


## Reference(s): <br>
- [Ccsinfo Skill Page](https://clawhub.ai/myakove/skills/ccsinfo) <br>
- [ccsinfo CLI Commands Reference](references/cli-commands.md) <br>
- [ccsinfo Server Documentation](https://github.com/myk-org/ccsinfo) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands; ccsinfo CLI commands may return text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the ccsinfo CLI, CCSINFO_SERVER_URL, and network access to a ccsinfo server.] <br>

## Skill Version(s): <br>
0.1.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
