## Description:

Pexels (pexels.com). Use this skill for ANY Pexels request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Pexels photos and videos, browse curated or popular media, inspect collections, and retrieve photo or video metadata through an OOMOL-connected Pexels account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute system-level code.

Mitigation: Do not let the agent run pipe-to-shell or Invoke-Expression installers automatically; install the oo CLI through a verified package or separately downloaded and checked installer.

Risk: Connector commands rely on an authenticated OOMOL-connected Pexels account and may fail when credentials, scopes, app readiness, or billing are not current.

Mitigation: Run setup or connection steps only after a matching command failure, and have the user resolve authentication, connection, scope, or billing issues explicitly.

## Reference(s):

- [ClawHub Pexels Skill Page](https://clawhub.ai/oomol/skills/oo-pexels)
- [Pexels Homepage](https://www.pexels.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas and run Pexels read actions with JSON payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
