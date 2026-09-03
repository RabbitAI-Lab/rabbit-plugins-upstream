## Description:

Get Biji operates a user's Get Biji account through OOMOL to read, create, update, share, search, and delete notes and knowledge base content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Get Biji notes and knowledge bases through an OOMOL-connected account, including read, search, write, share, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can inspect notes and knowledge bases in the connected Get Biji account.

Mitigation: Install and use this skill only when the agent is allowed to access the connected Get Biji account.

Risk: Write, sharing, update, and deletion actions can change or expose Get Biji content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing those actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-getnote)
- [Get Biji Homepage](https://www.biji.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Get Biji connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
