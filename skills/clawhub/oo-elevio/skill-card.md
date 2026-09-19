## Description:

Use this skill to search and read Elevio knowledge base articles and categories through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and agents use this skill to inspect Elevio action schemas and retrieve, list, or search Elevio knowledge base articles and categories through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could run arbitrary code if followed blindly.

Mitigation: Review the oo CLI installation path, install only from a trusted and versioned source with verification, avoid piping remote scripts directly into a shell, and do not run installers from an elevated shell unless independently verified.

Risk: The skill depends on an authenticated OOMOL-connected Elevio account and may fail when credentials are missing, expired, or lack required scopes.

Mitigation: Run setup or reconnection steps only after an action fails with an authentication, connection, scope, or credential-expiration error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-elevio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Elevio](https://elev.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Elevio connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
