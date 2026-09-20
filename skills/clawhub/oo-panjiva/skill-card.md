## Description:

Panjiva (panjiva.com). Use this skill for Panjiva requests involving reading, creating, and updating data through the OOMOL-connected Panjiva connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Panjiva data, inspect live connector schemas, run read actions for companies, shipments, HS codes, metadata, and trade metrics, and submit confirmed batch or bulk jobs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path directs users toward a remote installer script for the oo CLI.

Mitigation: Install the oo CLI only from trusted vendor instructions, verify the installer where possible, and do not allow an agent to run the remote installer command automatically.

Risk: The skill operates through OOMOL as a credentialed bridge to Panjiva.

Mitigation: Install only when the user is comfortable with OOMOL handling the Panjiva connection and credentials server-side.

Risk: Write-tagged batch and bulk actions can submit jobs that change Panjiva state or consume account resources.

Mitigation: Require user confirmation of the exact payload and expected effect before submitting any write-tagged batch or bulk job.

## Reference(s):

- [Panjiva homepage](https://panjiva.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Panjiva skill on ClawHub](https://clawhub.ai/oomol/skills/oo-panjiva)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata when commands are run.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
