## Description:

Plunk helps agents manage Plunk contacts, transactional email, event tracking, and email verification through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Plunk through an OOMOL-connected account for contact management, transactional email sending, event tracking, and email verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells the agent to run a remote installer script directly in the shell.

Mitigation: Review OOMOL's official installation instructions and verify the installer before allowing an agent to run the remote install command.

Risk: Plunk actions run through OOMOL as an intermediary.

Mitigation: Install only when that intermediary model is acceptable for the intended Plunk account and data.

Risk: The skill can send email, modify contacts, track events, and delete contacts.

Mitigation: Confirm write, email-sending, and deletion payloads with the user before execution, especially destructive contact deletion.

## Reference(s):

- [Plunk skill on ClawHub](https://clawhub.ai/oomol/skills/oo-plunk)
- [Plunk homepage](https://www.useplunk.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema checks before write, email-sending, or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
