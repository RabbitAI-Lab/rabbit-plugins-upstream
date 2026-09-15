## Description:

ORCID helps agents search public ORCID records and retrieve public researcher records or works through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up public ORCID profiles, works summaries, and search results without calling the ORCID API directly. It is suited for researcher discovery and bibliographic context gathering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unreviewed code if run blindly.

Mitigation: Use a verified, pinned, or manually reviewed installation path for the oo CLI before allowing an agent to use this skill.

## Reference(s):

- [ClawHub ORCID skill page](https://clawhub.ai/oomol/skills/oo-orcid)
- [ORCID homepage](https://orcid.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused ORCID actions return public record, works, or search data through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
