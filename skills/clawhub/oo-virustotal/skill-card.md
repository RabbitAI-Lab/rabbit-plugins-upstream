## Description:

Helps agents use VirusTotal through OOMOL's oo CLI to retrieve reports, search objects, submit scans, upload files, and manage comments or votes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to ask an agent to inspect VirusTotal reports, analyses, comments, votes, relationships, and metadata, or to submit scans and uploads after confirming state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts without checksum or signature verification.

Mitigation: Review the oo CLI installation path before installing; prefer a verified package-manager or documented installer flow and inspect downloaded scripts.

Risk: Write actions can upload files, submit URLs, rescan files, add comments, or cast votes in VirusTotal.

Mitigation: Confirm the exact action, target, payload, and effect with the user before running state-changing commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-virustotal)
- [VirusTotal homepage](https://www.virustotal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when run with --json; state-changing VirusTotal actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
