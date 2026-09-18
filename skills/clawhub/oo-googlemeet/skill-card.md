## Description:

Google Meet (workspace.google.com). Use this skill for ANY Google Meet request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Google Meet through an OOMOL-connected account, including creating and updating Meet spaces and retrieving conference records, participants, recordings, transcripts, and smart notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote installer commands that fetch and execute shell or PowerShell content.

Mitigation: Install the oo CLI through a verified or user-reviewed path and do not let an agent run remote installer pipelines automatically.

Risk: The end_active_conference action can change Google Meet state but is not tagged as write or destructive in the artifact.

Mitigation: Require explicit user confirmation of the target Meet space and intended effect before ending an active conference.

## Reference(s):

- [ClawHub Google Meet skill page](https://clawhub.ai/oomol/skills/oo-googlemeet)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Meet homepage](https://workspace.google.com/products/meet/)
- [OOMOL Google Meet connection settings](https://console.oomol.com/app-connections?provider=googlemeet)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
