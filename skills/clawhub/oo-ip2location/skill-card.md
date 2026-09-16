## Description:

This skill helps agents use IP2Location.io through an OOMOL-connected account to retrieve IP geolocation, domain WHOIS, and hosted-domain data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run IP2Location.io lookups from an agent workflow, including IP geolocation, domain WHOIS, and hosted-domain discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad access to run any oo CLI command, which is wider than its read-oriented IP2Location.io lookup purpose.

Mitigation: Use it only in environments where broad oo CLI access to the connected OOMOL session is acceptable, and review commands before execution.

Risk: The setup guidance includes direct remote installer commands that execute immediately.

Mitigation: Prefer a verified or package-manager installation path for the oo CLI, or inspect installer scripts before running them.

Risk: Lookup actions send queried IP addresses or domains through the connected OOMOL and IP2Location.io services.

Mitigation: Avoid submitting sensitive IP addresses or domains unless the user has approved the lookup and the connected account policies allow it.

## Reference(s):

- [IP2Location.io homepage](https://www.ip2location.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; requires an OOMOL account connected to IP2Location.io.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
