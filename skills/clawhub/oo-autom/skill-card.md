## Description:

Autom (autom.dev). Use this skill for Autom search and account-usage requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Autom data, including supported Google countries, languages, locations, and current account usage through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path asks users to run remote installer scripts for the oo CLI, which the security evidence flags for review before installation.

Mitigation: Prefer a pinned package or verified installer source, and avoid running remote shell installers from an elevated shell unless the source has been independently verified.

Risk: The skill can query Autom usage, account metadata, and API-key metadata through the connected OOMOL account.

Mitigation: Review the connected Autom account permissions and only connect accounts whose metadata can be exposed to the agent workflow.

## Reference(s):

- [Autom homepage](https://www.autom.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
