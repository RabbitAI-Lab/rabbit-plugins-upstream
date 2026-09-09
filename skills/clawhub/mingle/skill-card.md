## Description:

Find people through your agent. Tell your agent who you're looking for and Mingle helps find the right person through their agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

People using agent-assisted networking use Mingle to draft approved intent cards, search for relevant people, manage introductions, and coordinate mutual fit checks with human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation uses an npm-provided MCP server that can modify Claude Desktop or Cursor configuration.

Mitigation: Use a pinned, reviewed MCP package version and inspect generated client configuration before relying on it.

Risk: The skill can maintain persistent agent integration state and a Mingle identity under the user's home directory.

Mitigation: Install only when persistent identity and configuration files are acceptable, and review or remove files under ~/.mingle if disabling the skill.

Risk: Background checks and fit autonomy can create network activity or limited disclosure behavior after user opt-in.

Mitigation: Leave background checks and fit autonomy disabled unless explicitly desired, and pause or turn them off when the networking task is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeoess/skills/mingle)
- [Publisher profile](https://clawhub.ai/user/aeoess)
- [Mingle MCP npm package](https://www.npmjs.com/package/mingle-mcp)
- [Mingle landing page](https://aeoess.com/mingle.html)
- [Mingle API](https://api.aeoess.com)
- [Parent protocol](https://aeoess.com)
- [Declared open source repository](https://github.com/aeoess/mingle-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tool names, shell commands, and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should ask for explicit user approval before publishing cards, making introductions, or disclosing sensitive fit information.]

## Skill Version(s):

3.2.3 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
