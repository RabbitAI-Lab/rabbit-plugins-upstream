## Description:

Mailsoftly (mailsoftly.com). Use this skill for ANY Mailsoftly request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Mailsoftly through an OOMOL-connected account, including listing, searching, creating, and updating contacts and contact lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running mutable remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing, prefer a verified or package-manager installation method, and avoid running pipe-to-shell commands from an elevated shell.

Risk: Mailsoftly write actions can create or update contacts and contact lists in the connected account.

Mitigation: Confirm exact write payloads and expected account changes with the user before running actions tagged as write or destructive.

## Reference(s):

- [Mailsoftly homepage](https://mailsoftly.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailsoftly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing Mailsoftly write payloads.]

## Skill Version(s):

1.0.2 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
