## Description:

2Chat (2chat.co) helps agents read, create, and update 2Chat data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate 2Chat from an OOMOL-connected account, including listing contacts and webhooks, checking account usage, testing API credentials, and creating contacts after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote installer commands executed directly in a shell.

Mitigation: Review setup commands before installation and prefer a versioned, signed, or checksum-verified oo CLI source.

Risk: The create_contact action changes 2Chat data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [2Chat homepage](https://2chat.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twochat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before building action payloads; OOMOL handles 2Chat credentials outside the agent output.]

## Skill Version(s):

1.0.3 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
