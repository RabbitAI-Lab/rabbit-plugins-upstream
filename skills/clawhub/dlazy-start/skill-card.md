## Description:

Quickstart for AI orchestrators driving @dlazy/cli through install, authentication, capability discovery, cloud and local tool invocation, async polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI orchestrator operators use this skill to install and authenticate @dlazy/cli, inspect available tools, invoke cloud and local tools, poll asynchronous jobs, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on floating @dlazy/cli installs through npm or npx.

Mitigation: Prefer pinned package versions and review package changes before use.

Risk: The CLI can use API keys and stores configuration under the user's home directory.

Mitigation: Keep API keys out of logs and chat transcripts, and use environment or config handling appropriate for the workspace.

Risk: The CLI calls external dlazy network services and may invoke paid generation tools.

Mitigation: Trust the service before installing, inspect tool cost information with dlazy tools describe, and announce provider, model, and cost before paid calls.

Risk: The --save option writes generated or downloaded assets to local paths.

Mitigation: Verify save destinations before execution to avoid overwriting or placing files in unintended locations.

Risk: Browser-cookie use can expose a signed-in browser session to a downloader workflow.

Mitigation: Allow cookies_from_browser only when the user explicitly intends that site-specific signed-in session to be used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dlazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source metadata link](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI usage patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to verify available tools with dlazy tools list and dlazy tools describe before invoking commands.]

## Skill Version(s):

2.0.19 (source: server release evidence, created 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
