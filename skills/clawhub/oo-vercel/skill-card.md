## Description:

Enables agents to operate Vercel through OOMOL's oo CLI connector for reading, creating, updating, and deleting Vercel resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Vercel projects, deployments, domains, teams, environment variables, webhooks, and runtime logs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path and do not run remote installer commands blindly.

Risk: The OOMOL connector brokers Vercel action payloads for the connected account.

Mitigation: Install only when the user trusts OOMOL for the relevant Vercel account and review payloads before execution.

Risk: Some supported Vercel actions can write, overwrite, or delete resources.

Mitigation: Require explicit approval for every write or destructive action and confirm the exact target and payload before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vercel)
- [Vercel homepage](https://vercel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Vercel provider; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
