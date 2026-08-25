## Description:

百积木平台 helps agents operate Baijimu through the local `baijimu` CLI for authentication, capability discovery, workspaces, project files and Git, agent sessions, model credentials, platform apps, local Connector workflows, and Partner API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to discover and run supported Baijimu CLI workflows while preserving the local CLI help and versioned documentation as the source of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can initiate Baijimu operations with business side effects, including writes, publishing, deletion, paid operations, or external message sends.

Mitigation: Review commands before execution, require explicit authorization for destructive or cost-bearing actions, read current state first, and verify results after execution.

Risk: Authentication flows and model credential operations can expose sensitive tokens or credential responses.

Mitigation: Do not ask the agent to reveal tokens or full credential responses, and do not directly edit CLI authentication files, Bridge Agent configuration, Connector installation directories, or management tokens.

Risk: Using stale assumptions about CLI commands or documentation can cause incorrect platform actions.

Mitigation: Confirm the installed CLI version, inspect `baijimu` capability output and command help, and use only fixed version documentation returned by the local CLI.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/momoplan/skills/baijimu-platform)
- [Baijimu Platform Skill Homepage](https://github.com/momoplan/baijimu-platform-skill)
- [Baijimu Documentation](https://docs.baijimu.com/)
- [Baijimu CLI Documentation](https://docs.baijimu.com/cli/)
- [Baijimu Partner API](https://docs.baijimu.com/integration/api/)
- [Baijimu Projects Concepts](https://docs.baijimu.com/concepts/projects/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline CLI commands and JSON handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve command results, stable IDs, verification evidence, and unresolved version, authentication, or permission issues.]

## Skill Version(s):

1.6.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
