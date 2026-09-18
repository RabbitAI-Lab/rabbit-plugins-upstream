## Description:

IP2WHOIS enables agents to perform domain WHOIS lookups and list hosted domains through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve IP2WHOIS data through an OOMOL-connected account for domain registration lookups and hosted-domain searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified internet installer commands that can execute local code.

Mitigation: Review CLI installation manually and prefer a verified official package, pinned release, signed installer, or checksum-verified download; do not allow an agent to run curl-to-bash or irm-to-iex installer commands automatically.

Risk: Connector actions depend on authentication, account connection, and billing state.

Mitigation: Run setup, connection, or billing steps only after a matching command failure and keep normal WHOIS lookup actions separate from account setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ip2whois)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON data]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; first-time setup guidance is conditional on auth, connection, or billing errors.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
