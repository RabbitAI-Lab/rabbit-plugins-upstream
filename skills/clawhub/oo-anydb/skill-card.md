## Description:

AnyDB lets agents read, create, update, list, and search AnyDB records through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with AnyDB records from an agent session, including read and search workflows plus confirmed create and update operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute mutable remote installer scripts directly in a shell.

Mitigation: Review the setup path before installation and prefer a verified, versioned, or package-managed oo CLI install method outside an automated agent flow.

Risk: create_record and update_record actions can change AnyDB state.

Mitigation: Confirm the exact JSON payload and expected effect with the user before allowing either write action.

## Reference(s):

- [ClawHub AnyDB Skill](https://clawhub.ai/oomol/skills/oo-anydb)
- [AnyDB homepage](https://www.anydb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires oo CLI authentication and an AnyDB connection; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
