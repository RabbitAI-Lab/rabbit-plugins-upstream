## Description:

Operate Tailscale through an OOMOL-connected account to read, create, update, and delete tailnet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and administrators use this skill to inspect Tailscale action schemas, run tailnet administration actions, and manage devices, users, keys, DNS, webhooks, policy files, posture integrations, services, and settings through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup examples download and immediately execute remote installer scripts.

Mitigation: Prefer a verified package or download-and-check installation process before running the oo CLI installer.

Risk: Write and destructive actions can change or remove Tailscale tailnet resources.

Mitigation: Approve writes or deletions only after confirming the exact action, target, and JSON payload.

Risk: Some create and rotate actions can return credentials, client secrets, or webhook signing secrets.

Mitigation: Treat returned secrets as sensitive and avoid exposing them in shared logs, tickets, or transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tailscale)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Tailscale homepage](https://tailscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
