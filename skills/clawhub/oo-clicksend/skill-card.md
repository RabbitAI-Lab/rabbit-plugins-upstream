## Description:

ClickSend lets an agent read, create, update, and delete ClickSend data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage ClickSend account data, contacts, contact lists, SMS pricing, and SMS sending from an agent through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad oo CLI authority.

Mitigation: Review the skill before installing and prefer narrower permissions limited to ClickSend connector commands.

Risk: The first-time setup section includes pipe-to-shell installer commands.

Mitigation: Verify and trust the OOMOL installer before running it, or use safer installation steps with versioning or checksum verification where available.

Risk: The skill can create, update, send, or delete ClickSend resources.

Mitigation: Confirm exact payloads and targets before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clicksend)
- [ClickSend Homepage](https://www.clicksend.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ClickSend connector command plans, schema inspection commands, and confirmation prompts for state-changing actions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
