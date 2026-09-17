## Description:

This skill enables an agent to query Plausible Analytics data and record Plausible events through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect Plausible Analytics connector schemas, run stats queries for connected sites, and record pageview or custom events after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer snippets can execute remote setup code locally if used without review.

Mitigation: Run installer commands only after trusting OOMOL's installer source and verifying the install path.

Risk: The record_event action can write pageview or custom event data to Plausible Analytics.

Mitigation: Require explicit confirmation of the exact site, event name, URL, and properties before running record_event.

Risk: Credential or connection setup may fail or lack required scopes.

Mitigation: Use normal read-only oo connector commands first and fall back to authentication or connection setup only when a command fails for that reason.

## Reference(s):

- [Plausible Analytics](https://plausible.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plausible-analytics)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
