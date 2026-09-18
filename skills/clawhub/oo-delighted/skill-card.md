## Description:

Delighted helps agents read, create, update, and delete Delighted data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Delighted from an agent workflow, including people management, unsubscribe and delete workflows, survey response listing, and NPS or metrics retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that should be reviewed before use.

Mitigation: Install the oo CLI through verified official release instructions and prefer pinned versions, checksums, or signed packages.

Risk: Write, delete, and unsubscribe actions can change or remove Delighted account data.

Mitigation: Confirm the exact action, payload, and target with the user before executing state-changing or destructive commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-delighted)
- [Delighted Homepage](https://delighted.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing and destructive Delighted actions require confirmation of the exact payload and target before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
