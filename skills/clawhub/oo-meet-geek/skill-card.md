## Description:

MeetGeek (meetgeek.ai). Use this skill for MeetGeek requests that search, read, and retrieve meeting data through the OOMOL-connected MeetGeek connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MeetGeek through an OOMOL-connected account, including listing meetings and retrieving meeting details, summaries, transcripts, highlights, insights, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unpinned remote installer scripts for the oo CLI.

Mitigation: Prefer a verified package or documented release path, and review the installer source before executing remote scripts.

Risk: MeetGeek connector access is handled through OOMOL's connector flow.

Mitigation: Use the skill only when OOMOL handling the connector flow and connected MeetGeek account data is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-meet-geek)
- [MeetGeek homepage](https://meetgeek.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
