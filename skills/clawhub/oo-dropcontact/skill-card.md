## Description:

Dropcontact helps agents operate Dropcontact through an OOMOL-connected account for retrieving enrichment results and submitting contact enrichment requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Dropcontact through OOMOL, including retrieving pending or completed enrichment results and submitting up to 250 contacts for asynchronous email verification and enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run unverified remote installer scripts in a shell.

Mitigation: Install the oo CLI only from a verified, version-pinned, signed, or inspectable source before using the skill.

Risk: The submit_enrichment action changes Dropcontact state by submitting contact data for asynchronous enrichment.

Mitigation: Inspect the live action schema and confirm the exact write payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dropcontact)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Dropcontact Homepage](https://www.dropcontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Dropcontact connector actions through the oo CLI after inspecting the live action schema and confirming write payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
