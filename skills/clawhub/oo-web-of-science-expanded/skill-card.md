## Description:

Web of Science Expanded (clarivate.com). Use this skill for Web of Science Expanded search and retrieval tasks through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to search Web of Science Expanded records, retrieve documents, inspect citation relationships, and generate citation reports through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes online installer commands that can execute code from remote URLs.

Mitigation: Review and verify the oo CLI installer source before running it; prefer a version-pinned, signed, or checksum-checked installation path, and do not allow an agent to run curl|bash or irm|iex blindly.

Risk: The skill depends on an OOMOL-connected account to access Web of Science Expanded.

Mitigation: Use the skill only when the user trusts OOMOL for this connector and intends to use that account connection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-web-of-science-expanded)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Web of Science Expanded Homepage](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running Web of Science Expanded actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
