## Description:

Crunchbase helps agents search and read Crunchbase data through the OOMOL-connected Crunchbase connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to autocomplete Crunchbase entities and retrieve or search organization, acquisition, and IPO records through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer scripts that may be run directly in a shell.

Mitigation: Install only after trusting OOMOL, and prefer a verified package or an inspected pinned installer without using an elevated shell unless required.

Risk: Connector payloads can be incorrect if built from assumptions instead of the current action contract.

Mitigation: Inspect the live connector schema before each action and submit JSON that matches the returned schema.

Risk: Future connector actions tagged write or destructive could change or remove Crunchbase data.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crunchbase)
- [Crunchbase homepage](https://www.crunchbase.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Crunchbase connection](https://console.oomol.com/app-connections?provider=crunchbase)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
