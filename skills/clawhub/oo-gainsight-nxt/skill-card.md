## Description:

Gainsight NXT helps agents read, create, update, and delete Gainsight NXT Company records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Gainsight NXT Company records from an agent, including querying records and preparing approved create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded code directly.

Mitigation: Review the install path first and prefer a verified, version-pinned oo CLI installation method.

Risk: The skill can read, create, update, and delete Gainsight Company records.

Mitigation: Connect only accounts and API keys approved for this access, inspect schemas before use, and require explicit user approval for write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gainsight-nxt)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gainsight NXT homepage](https://www.gainsight.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require explicit user approval.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
