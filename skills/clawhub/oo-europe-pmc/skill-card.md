## Description:

Europe PMC (europepmc.org). Use this skill for ANY Europe PMC request - searching and reading data. Whenever a task involves Europe PMC, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and retrieve Europe PMC publications, preprints, grants, annotations, citations, references, full-text XML, and article status through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time use may require installing the oo CLI or signing in to OOMOL.

Mitigation: Run setup only after a command fails for a missing CLI or authentication error, then retry the intended action.

Risk: Future connector actions marked write or destructive could change or remove data.

Mitigation: Review the live action schema and confirm the exact payload and effect with the user before running write or destructive actions.

## Reference(s):

- [Europe PMC homepage](https://europepmc.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-europe-pmc)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
