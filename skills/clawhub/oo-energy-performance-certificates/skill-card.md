## Description:

Energy Performance Certificates (get-energy-performance-data.communities.gov.uk). Use this skill for ANY Energy Performance Certificates request - searching and reading data. Whenever a task involves Energy Performance Certificates, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search domestic, non-domestic, and display Energy Performance Certificates and fetch certificate details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands such as curl piped to bash and PowerShell irm piped to iex.

Mitigation: Prefer a verified, versioned installer or inspect and validate the installer script before execution.

Risk: The skill depends on the OOMOL oo CLI and server-side connector credentials.

Mitigation: Install only if you trust OOMOL, use the documented schema inspection workflow, and avoid re-running setup or auth commands unless an action fails with a matching error.

## Reference(s):

- [Energy Performance Certificates homepage](https://get-energy-performance-data.communities.gov.uk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-energy-performance-certificates)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
