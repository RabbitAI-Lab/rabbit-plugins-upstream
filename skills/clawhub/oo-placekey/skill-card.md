## Description:

Placekey helps agents query Placekey data through the OOMOL oo CLI for address geocoding, single-location Placekey lookups, and bulk Placekey lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve addresses, retrieve Placekey identifiers and enrichment fields, and run bulk Placekey lookups through an OOMOL-connected Placekey account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes inline remote installer commands that can execute code on the user's machine.

Mitigation: Install the oo CLI only from verified official releases or package-manager instructions, and avoid running installer one-liners blindly.

Risk: Placekey requests are routed through OOMOL as the credential-handling intermediary.

Mitigation: Install only when the user accepts OOMOL's role as the intermediary and connects Placekey deliberately.

## Reference(s):

- [Placekey homepage](https://www.placekey.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema checks before payload construction; bulk lookup supports up to 100 locations per request.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
