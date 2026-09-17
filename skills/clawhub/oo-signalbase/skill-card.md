## Description:

Signalbase skill for searching and reading company profiles, investors, and market signals through the OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Signalbase company, investor, acquisition, funding, hiring, and job-change data through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup asks users to run remote installer commands for the oo CLI.

Mitigation: Install only from trusted OOMOL distribution paths and prefer a verified package-manager or documented installation method before using the connector.

Risk: Signalbase actions depend on authenticated OOMOL account state, connector permissions, and billing status.

Mitigation: Run setup or connection steps only after an auth, scope, credential, app, or billing error, and verify account state before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-signalbase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Signalbase Homepage](https://www.trysignalbase.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema checks, JSON payloads, and summarized Signalbase results.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
