## Description:

Enables an agent to read Agility CMS content and site data through OOMOL's `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to retrieve Agility CMS content items, content lists, pages, sitemaps, and content models from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts locally.

Mitigation: Install the `oo` CLI manually from a separately verified source before using the skill; do not let an agent automatically run `curl | bash` or `irm | iex` installer commands.

Risk: Connector actions depend on live schemas and OOMOL-connected credentials, so stale assumptions could produce incorrect payloads or failed requests.

Mitigation: Inspect the connector schema for the selected action immediately before building a payload and use first-time setup only after an authentication or connection failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agility)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Agility CMS homepage](https://agilitycms.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
