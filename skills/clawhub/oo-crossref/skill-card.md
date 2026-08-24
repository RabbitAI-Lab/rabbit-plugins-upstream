## Description:

Crossref connector skill for searching, reading, and exporting Crossref metadata through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Crossref records, search works, retrieve DOI metadata, match formatted references, and export citations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crossref requests are routed through OOMOL's oo CLI and connected account.

Mitigation: Install and use the skill only when routing Crossref metadata requests through OOMOL is acceptable for the user's workflow.

Risk: First-time setup may install the oo CLI and require OOMOL sign-in, a Crossref connection, or billing credits.

Mitigation: Perform setup only after a matching command failure and keep authentication, connection, and billing actions explicit to the user.

## Reference(s):

- [Crossref homepage](https://www.crossref.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Crossref skill page](https://clawhub.ai/oomol/skills/oo-crossref)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live action schemas and run oo CLI connector commands that return JSON responses.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
