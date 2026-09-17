## Description:

Cert Spotter helps agents inspect OOMOL connector schemas and run Cert Spotter actions for monitored domains and certificate issuance records through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cert Spotter monitored domains and review certificate issuance records through an OOMOL-connected CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes one-line remote script execution for installing the oo CLI.

Mitigation: Install the oo CLI through a verified, version-pinned method with signatures or checksums before running connector commands.

Risk: Write and destructive Cert Spotter actions can modify or delete monitored domain configuration.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or delete actions.

## Reference(s):

- [Cert Spotter homepage](https://sslmate.com/certspotter/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sslmate-cert-spotter-api)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
