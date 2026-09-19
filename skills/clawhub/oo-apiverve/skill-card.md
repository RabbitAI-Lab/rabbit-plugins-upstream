## Description:

APIVerve lets agents search and read APIVerve data through the OOMOL APIVerve connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run APIVerve utility, language, location, and travel-data actions through an OOMOL-connected account. It guides agents to inspect each live connector schema before sending JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI only from trusted OOMOL sources and prefer package-manager or installer flows with checksum or signature verification before running setup commands.

Risk: APIVerve connector calls depend on account credentials and billing state managed outside the skill.

Mitigation: Use the documented auth, connection, scope, and credit recovery steps only when connector commands fail for those specific reasons.

## Reference(s):

- [APIVerve homepage](https://apiverve.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apiverve)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to use oo connector schema and run commands; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
