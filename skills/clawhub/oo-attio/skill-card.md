## Description:

Attio helps agents inspect live action schemas and operate Attio CRM data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read Attio workspace metadata and records, and to create, update, upsert, or delete Attio records when the user has approved the requested change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup includes remote installer commands that should not be run blindly.

Mitigation: Use verified official installation steps and inspect installer behavior before running curl|bash or irm|iex commands.

Risk: Write and destructive Attio actions can create, update, upsert, or delete CRM records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving write or destructive actions.

Risk: Using the OOMOL connector grants access to an Attio workspace through the connected account.

Mitigation: Install only when comfortable granting OOMOL the required Attio access, and review token scopes or connection errors before retrying.

## Reference(s):

- [ClawHub Attio skill page](https://clawhub.ai/oomol/skills/oo-attio)
- [Attio homepage](https://attio.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema inspection commands and connector run commands for Attio actions.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
