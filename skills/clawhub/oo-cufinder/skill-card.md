## Description:

CUFinder helps agents search and read CUFinder enrichment data through the OOMOL oo connector instead of calling the CUFinder API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run CUFinder lookups for company enrichment, person enrichment, email enrichment, company domain discovery, and company-name resolution through an OOMOL-connected CUFinder account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell-install commands for the OOMOL CLI.

Mitigation: Review the OOMOL installer through official documentation and prefer a verified package or manually inspected installer before running installation commands.

Risk: Person and email enrichment can return sensitive professional contact data.

Mitigation: Use the skill only for authorized CUFinder enrichment tasks and limit submitted identifiers and returned data handling to the user's intended purpose.

Risk: Connector action schemas are live and may change over time.

Mitigation: Fetch the authoritative action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [CUFinder homepage](https://cufinder.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [CUFinder ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cufinder)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload/response patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.0 (source: evidence metadata and release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
