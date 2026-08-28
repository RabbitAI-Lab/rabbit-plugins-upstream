## Description:

Quickstart guidance for AI orchestrators using @dlazy/cli, covering installation, authentication, capability discovery, cloud and local tool invocation, asynchronous task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to guide Claude Code, Cursor, Codex, Copilot, or similar orchestrators through safe discovery and use of @dlazy/cli tools. It helps agents install and authenticate the CLI, inspect available tool schemas and costs, run cloud or local commands, poll long-running jobs, and recover from documented failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill suggests using local browser cookies for video-download troubleshooting, which may expose logged-in browser session data.

Mitigation: Require explicit user approval for the specific site and browser profile before allowing cookie access, and avoid copying or logging cookie material.

Risk: Global npm installation and optional runtime installers can change the local environment.

Mitigation: Review the package and runtime install commands before execution, prefer isolated environments where practical, and confirm Node and proxy settings with the user.

Risk: CLI authentication stores or accepts API keys and may send inputs to cloud endpoints.

Mitigation: Use approved secret handling, avoid printing API keys in logs, and confirm cloud-upload-sensitive inputs before invoking tools.

Risk: Cloud generation tools may incur costs or run long asynchronous jobs.

Mitigation: Run tool discovery and schema inspection first, disclose provider/model/cost shape before paid calls, and use dry-run validation when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is bilingual and includes command examples, discovery-first operating rules, and troubleshooting notes.]

## Skill Version(s):

2.0.10 (source: ClawHub release metadata; artifact frontmatter says 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
