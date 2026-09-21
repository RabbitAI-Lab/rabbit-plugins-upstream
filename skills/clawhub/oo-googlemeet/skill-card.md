## Description:

Google Meet enables an agent to read, create, and update Google Meet data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to manage Google Meet spaces and retrieve meeting artifacts such as conference records, participants, recordings, transcripts, transcript entries, and smart notes. The skill is intended for users who have connected Google Meet through OOMOL and want the agent to run schema-checked oo CLI actions on their behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute a remote oo CLI installer script without verification or clear user approval.

Mitigation: Review the installer path before use, prefer a trusted documented source with verification, and obtain user approval before running installer commands.

Risk: The skill can access Google Meet spaces, participants, recordings, transcripts, transcript entries, and smart notes through OOMOL-mediated credentials.

Mitigation: Connect Google Meet only after the user accepts the access model, confirm write actions before execution, and review scopes or account access if authorization errors occur.

## Reference(s):

- [ClawHub Google Meet skill page](https://clawhub.ai/oomol/skills/oo-googlemeet)
- [Google Meet homepage](https://workspace.google.com/products/meet/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from oo connector actions, including execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
