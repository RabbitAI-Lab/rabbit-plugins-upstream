## Description:

Use this skill for VirusTotal requests on virustotal.com, including reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to inspect VirusTotal reports, searches, comments, votes, metadata, and relationships through an OOMOL-connected account. It can also submit URLs, upload files, request rescans, add comments, and submit votes when the user approves write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute shell scripts directly.

Mitigation: Install the oo CLI through a verified package, pinned release, checksum or signature checked download, or manual installer inspection instead of allowing automatic pipe-to-shell execution.

Risk: Write actions can change VirusTotal state by adding comments or votes, submitting URLs, uploading files, or requesting rescans.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-virustotal)
- [VirusTotal homepage](https://www.virustotal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON action payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return VirusTotal connector results as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
