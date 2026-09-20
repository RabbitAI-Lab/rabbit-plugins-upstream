## Description:

Radar (radar.com). Use this skill for Radar requests involving search and data retrieval through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Radar geocoding, address autocomplete, IP geocoding, reverse geocoding, and nearby place search actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer one-liners for the oo CLI without integrity checks.

Mitigation: Install the oo CLI only from a trusted official package or verified artifact, and do not allow an agent to run remote installer one-liners automatically.

Risk: Radar actions depend on an OOMOL-connected Radar account and may fail when authentication, scopes, credentials, app setup, or billing are not ready.

Mitigation: Run setup steps only after a matching command failure, and have the user resolve account connection or billing issues before retrying.

## Reference(s):

- [Radar homepage](https://radar.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Radar actions are read/search oriented; inspect the live action schema before constructing payloads.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
