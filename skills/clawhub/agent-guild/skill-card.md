## Description:

Helps trusted local AI assistants share user preferences, project rules, memory, and handoffs through local files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

People using multiple trusted AI assistants with local file access can maintain shared preferences, recall past work, and pass context between assistants on their devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared local memory is plaintext and accessible to trusted agents with file access.

Mitigation: Use only with trusted agents and do not store secrets in shared memory.

Risk: Remote installer execution and automatic update application can replace local code.

Mitigation: Install from a reviewed local checkout or package instead of piping remote scripts to a shell; keep updates in check or off mode unless code replacement is explicitly approved.

Risk: Optional adoption or root linking can move or expose skills, tools, MCP configuration, and memory beyond the basic shared-memory setup.

Mitigation: Begin with memory-only onboarding; preview any wider migration and apply only the scope explicitly authorized by the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Publisher-listed project homepage (not verified import provenance)](https://github.com/dqsjqian/agent-guild)
- [Onboarding guide](artifact/references/ONBOARDING.md)
- [Security and data handling](artifact/references/SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown guidance; optional local Markdown and JSON memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local shared memory requires filesystem access and has no built-in encryption or per-agent access controls.]

## Skill Version(s):

3.12.0 (source: server-resolved ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
