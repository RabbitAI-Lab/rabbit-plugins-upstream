## Description:

Brave Search (search.brave.com). Use this skill for Brave Search requests that involve searching and reading data through the OOMOL-connected connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Brave web, image, news, and video searches through the OOMOL-connected oo CLI and receive structured search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts in a local shell without verification.

Mitigation: Review the oo CLI installer source, prefer a pinned or package-manager installation path when available, and avoid running installer commands from an elevated shell.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-brave-search)
- [Brave Search Homepage](https://search.brave.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
