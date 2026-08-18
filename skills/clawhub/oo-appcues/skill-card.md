## Description:

Appcues helps agents operate an OOMOL-connected Appcues account through the oo CLI connector to retrieve, list, publish, and unpublish Flow 2.0 experiences and content tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Appcues Flow 2.0 experiences and content tags through an OOMOL-connected account without handling raw Appcues tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing and unpublishing Appcues flows can change live product experiences, and the security evidence notes that unpublishing is not labeled as a write action in the artifact.

Mitigation: Require explicit user confirmation for both publish_flow and unpublish_flow, including the target flow, payload, and intended effect, before running the connector action.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Appcues homepage](https://www.appcues.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL server-side credentials; inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
