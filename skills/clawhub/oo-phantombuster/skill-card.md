## Description:

PhantomBuster (phantombuster.com). Use this skill for ANY PhantomBuster request — reading, creating, and updating data. Whenever a task involves PhantomBuster, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect PhantomBuster schemas, read agent and container data, launch agents, and stop running agents through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends installing the OOMOL CLI from web-hosted scripts.

Mitigation: Prefer a verified or package-manager installation path and review the installer source before execution.

Risk: Launching or stopping PhantomBuster agents can change account state, spend credits, or run automation.

Mitigation: Require explicit user confirmation for launch_agent and stop_agent payloads before executing commands.

## Reference(s):

- [PhantomBuster ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-phantombuster)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [PhantomBuster Homepage](https://phantombuster.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing PhantomBuster action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
