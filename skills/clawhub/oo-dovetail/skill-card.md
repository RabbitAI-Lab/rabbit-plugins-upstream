## Description:

Dovetail helps agents read, create, update, list, retrieve, and export Dovetail data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with connected OOMOL and Dovetail accounts use this skill to operate Dovetail records and projects from an agent session while avoiding direct API-token handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct shell execution of remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a trusted, verified method and do not allow an agent to run installer commands automatically.

Risk: The skill can create and update Dovetail data records.

Mitigation: Confirm the exact action payload and intended effect with the user before any write action runs.

Risk: Dovetail account access depends on OOMOL as the credential and connector intermediary.

Mitigation: Use the skill only when the user trusts OOMOL for the connected Dovetail account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dovetail)
- [Dovetail Homepage](https://dovetail.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, markdown]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
