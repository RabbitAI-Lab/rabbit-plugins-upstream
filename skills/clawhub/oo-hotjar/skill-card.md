## Description:

This skill helps agents operate Hotjar through the OOMOL oo CLI to list and retrieve surveys and responses, and to submit organization user lookup requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents working with a connected Hotjar account use this skill to inspect live action schemas, retrieve survey data and responses, and submit organization user lookup requests through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run the remote installer automatically; download from an official source, inspect it, and verify integrity where possible before approving installation.

Risk: The submit_user_lookup action can change Hotjar state and may delete matching user data when deleteAllHits is enabled.

Mitigation: Confirm the exact action, payload, target account, and deleteAllHits setting with the user before running the command.

Risk: Hotjar operations run through an OOMOL-connected account.

Mitigation: Install and use the skill only when the user trusts OOMOL and has confirmed the connected account and scopes are appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hotjar)
- [Hotjar Homepage](https://www.hotjar.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running Hotjar actions; command results can be returned as JSON.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
