## Description:

Scrapfly lets agents search and read data through the OOMOL Scrapfly connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Scrapfly connector schemas, scrape public URLs, and retrieve Scrapfly monitoring metrics through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI from official documentation with a pinned release and checksum or signature verification where available before running Scrapfly actions.

Risk: Connector payloads built without the live schema may be malformed or target the wrong Scrapfly action parameters.

Mitigation: Run `oo connector schema "scrapfly" --action "<action_name>"` before constructing each action payload.

## Reference(s):

- [Scrapfly homepage](https://scrapfly.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrapfly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Scrapfly connector JSON responses through the oo CLI, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
