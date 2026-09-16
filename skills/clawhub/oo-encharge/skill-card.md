## Description:

Encharge helps agents read, create, and update Encharge data through an OOMOL-connected account using the oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect live Encharge action schemas and run Encharge connector actions, including sending transactional email, through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing code on a user's machine.

Mitigation: Review the installer path before installing; prefer a signed, versioned, or package-manager source, or download and verify the installer before execution.

Risk: The send_email action changes Encharge account state by sending transactional email.

Mitigation: Confirm the exact email payload and intended effect with the user before running write actions.

Risk: Connector requests built without the current action schema can use incorrect input fields.

Mitigation: Inspect the live action schema with the oo CLI before constructing each request payload.

## Reference(s):

- [ClawHub Encharge Skill](https://clawhub.ai/oomol/skills/oo-encharge)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Encharge](https://encharge.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents should inspect live connector schemas before constructing JSON payloads and confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
