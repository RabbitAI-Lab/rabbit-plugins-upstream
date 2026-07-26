## Description: <br>
Run and script the XMTP CLI for testing, debugging, and interacting with XMTP conversations, groups, and messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[humanagent](https://clawhub.ai/user/humanagent) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to install, configure, and operate the XMTP CLI for messaging, group management, synchronization, diagnostics, permissions, and content-type demonstrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: XMTP wallet keys, database encryption keys, and .env files can expose sensitive account or messaging access if shared or committed. <br>
Mitigation: Prefer dev or ephemeral keys for testing, keep .env files out of git and shared logs, and avoid passing real private keys on the command line where possible. <br>
Risk: Messaging, group creation, and permission changes may affect real recipients or groups if commands are run against the wrong target. <br>
Mitigation: Double-check recipients, group IDs, environment, and permission settings before sending messages, creating groups, or changing permissions. <br>


## Reference(s): <br>
- [XMTP documentation](https://docs.xmtp.org) <br>
- [XMTP debug agents documentation](https://docs.xmtp.org/agents/debug-agents) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI commands and environment-variable examples for XMTP setup, messaging, debugging, synchronization, groups, permissions, and content demos.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
