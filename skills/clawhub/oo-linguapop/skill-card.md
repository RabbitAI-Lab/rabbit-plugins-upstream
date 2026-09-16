## Description:

Linguapop lets an agent operate the Linguapop connector through the OOMOL-connected oo CLI for reading, creating, and updating Linguapop data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Linguapop placement-test workflows through their connected OOMOL account, including listing available languages and creating placement-test invitations. The skill directs agents to inspect live action schemas and confirm state-changing invitation payloads before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to execute remote installer scripts directly.

Mitigation: Review the installer path before use, prefer an official versioned signed or checksum-verified oo CLI installation method, and avoid running installer commands from an elevated shell.

Risk: The skill can create Linguapop placement-test invitations through a write action.

Mitigation: Confirm the exact invitation payload and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linguapop)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Linguapop homepage](https://www.linguapop.eu/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request JSON payloads for oo connector actions; write actions require confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
