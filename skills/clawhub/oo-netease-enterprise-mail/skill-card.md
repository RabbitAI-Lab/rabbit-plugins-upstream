## Description:

Use NetEase Enterprise Mail through OOMOL for mailbox requests such as reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected NetEase Enterprise Mail account through OOMOL, including folder discovery, message search, safe retrieval, sending, replying, forwarding, moving, read-state changes, attachment download, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute code on the user's machine.

Mitigation: Use a verified, signed, or package-manager installation path for the oo CLI and avoid running remote installer scripts blindly.

Risk: Write actions can send, reply, forward, move, or change the read state of mailbox messages.

Mitigation: Confirm the exact payload and expected mailbox effect before approving any write action.

Risk: The delete action can remove an email from a folder.

Mitigation: Require explicit approval for the specific target message and folder before running deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netease-enterprise-mail)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [NetEase Enterprise Mail homepage](https://qiye.163.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect connector schemas or run NetEase Enterprise Mail actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
