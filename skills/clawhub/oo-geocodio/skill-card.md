## Description:

Geocodio (geocod.io) enables agents to geocode addresses and reverse geocode coordinates through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Geocodio connector schemas and run single or batch geocoding and reverse-geocoding actions from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands that execute downloaded scripts directly.

Mitigation: Install the oo CLI only from trusted, version-pinned sources and verify checksums or signatures when available before running installer code.

Risk: Geocodio actions depend on an OOMOL-connected account and server-side credential handling.

Mitigation: Inspect the live action schema before requests, run setup only after authentication or connection failures, and avoid exposing raw credentials in prompts or payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-geocodio)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Geocodio homepage](https://www.geocod.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Geocodio connector result JSON returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
