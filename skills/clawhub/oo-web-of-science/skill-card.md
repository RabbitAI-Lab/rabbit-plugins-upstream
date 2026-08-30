## Description:

Web of Science (clarivate.com). Use this skill for ANY Web of Science request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, librarians, analysts, and agents supporting them use this skill to search Web of Science documents and journals, then retrieve records through an OOMOL-connected Web of Science account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on OOMOL account access and a connected Web of Science account.

Mitigation: Install and use it only when OOMOL and the connected Web of Science account are intended for the workflow.

Risk: Action payloads can be incorrect if the connector contract changes.

Mitigation: Review the live action schema before constructing payloads.

Risk: Optional CLI installation and account connection steps introduce trust and setup decisions.

Mitigation: Run setup steps only when needed and only after confirming OOMOL is trusted for the environment.

## Reference(s):

- [Web of Science homepage](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-web-of-science)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
