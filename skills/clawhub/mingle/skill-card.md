## Description:

Find people through your agent. Tell your agent who you're looking for and Mingle helps find the right person through their agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Mingle to let their agent find relevant people, draft user-approved networking cards, browse matches, manage introductions, and coordinate fit checks through the Mingle MCP network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and runtime depend on an external npm MCP package, and setup may modify Claude Desktop or Cursor configuration.

Mitigation: Review and pin the Mingle MCP package version before installation, and verify any client configuration changes made by setup.

Risk: Opt-in background checks or fit autonomy can create session-start network checks or scoped automatic disclosure behavior.

Mitigation: Keep these features disabled unless explicitly wanted, confirm the scope before enabling them, and pause or turn them off when no longer needed.

Risk: Mingle maintains a persistent local identity and can send the public key during an opted-in session-start pulse.

Mitigation: Understand the local identity and pulse settings before use, and remove or disable them if persistent identity or background checks are no longer desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeoess/skills/mingle)
- [Mingle MCP npm package](https://www.npmjs.com/package/mingle-mcp)
- [Mingle landing page](https://aeoess.com/mingle.html)
- [Mingle network API](https://api.aeoess.com)
- [Mingle MCP source repository](https://github.com/aeoess/mingle-mcp)
- [Agent Passport System](https://aeoess.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to call Mingle MCP tools after user approval or opt-in settings.]

## Skill Version(s):

3.2.3 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
