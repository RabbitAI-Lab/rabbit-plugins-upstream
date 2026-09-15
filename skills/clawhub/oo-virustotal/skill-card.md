## Description:

VirusTotal enables an agent to read, create, and update VirusTotal data through the OOMOL-connected oo CLI instead of calling the VirusTotal API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and agent users use this skill to query VirusTotal reports and relationships, search indicators, submit URLs or files, and perform guarded comments or votes through OOMOL's VirusTotal connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VirusTotal requests, submitted indicators, comments, votes, and uploaded files are routed through OOMOL as an intermediary.

Mitigation: Install and use the skill only when that intermediary is acceptable for the data being submitted or retrieved.

Risk: The first-time setup includes pipe-to-shell installer commands.

Mitigation: Prefer a verified, pinned, or package-manager-based installation path before using the oo CLI.

Risk: Write actions can submit URLs, upload files, add comments, or add votes in VirusTotal.

Mitigation: Confirm exact payloads and intended effects before uploads or other write actions.

## Reference(s):

- [VirusTotal](https://www.virustotal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
