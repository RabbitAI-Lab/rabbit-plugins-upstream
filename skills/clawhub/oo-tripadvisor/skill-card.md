## Description:

Tripadvisor guides agents to use the OOMOL Tripadvisor connector for searching locations, finding nearby places, and retrieving location details or photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to search Tripadvisor locations, retrieve location details, fetch photos, or find nearby locations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could run arbitrary code if fetched from an untrusted or compromised source.

Mitigation: Install the oo CLI through a verified, user-controlled process, and prefer the published install guide over directly piping remote scripts into a shell.

Risk: Tripadvisor requests are routed through OOMOL as an intermediary.

Mitigation: Use the skill only when the user is comfortable with OOMOL handling Tripadvisor requests through the connected account.

Risk: First-time setup can modify the local environment or require account connection and billing actions.

Mitigation: Run setup only after an authentication, connection, missing CLI, or billing error, and avoid proactive login or connection changes.

## Reference(s):

- [Tripadvisor Developers](https://www.tripadvisor.com/developers)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tripadvisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and PowerShell command blocks, JSON payload examples, and plain-text setup URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON responses returned by the oo CLI when Tripadvisor connector actions are executed.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
