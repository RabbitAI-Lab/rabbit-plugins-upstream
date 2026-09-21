## Description:

Buzzsprout helps agents manage podcasts, episodes, metadata, publishing workflows, and download reports through an OOMOL-connected Buzzsprout account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Buzzsprout through an OOMOL-connected account, including listing podcasts and episodes, creating or updating episodes, updating podcast metadata, and retrieving download reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute a remotely fetched installer script for the oo CLI.

Mitigation: Review the installer source independently and install the CLI only from a trusted OOMOL source before allowing an agent to use it.

Risk: Write and destructive Buzzsprout actions can create, publish, schedule, unpublish, or overwrite podcast data.

Mitigation: Require explicit user confirmation for the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Buzzsprout Skill Page](https://clawhub.ai/oomol/skills/oo-buzzsprout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Buzzsprout Homepage](https://www.buzzsprout.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI and a connected Buzzsprout account; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
