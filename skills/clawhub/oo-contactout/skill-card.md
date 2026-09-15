## Description:

ContactOut helps an agent use the OOMOL oo CLI to search, count, enrich, and verify ContactOut people and company data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run authorized ContactOut workflows through an OOMOL-connected account, including people and company search, enrichment, contact availability checks, email verification, and usage-stat retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installation commands for the oo CLI.

Mitigation: Install the oo CLI through a verifiable channel and review installer contents before running setup commands.

Risk: ContactOut actions can retrieve or check sensitive contact data such as email addresses, phone availability, and profile enrichment.

Mitigation: Run lookups only for authorized workflows with a lawful basis, clear user intent, and any required consent or policy approval.

Risk: Treating contact-data lookup actions as direct reads can encourage automatic use without considering privacy impact.

Mitigation: Confirm the purpose and identifiers before enrichment or contact-info retrieval, and inspect the live connector schema before sending payloads.

## Reference(s):

- [ContactOut homepage](https://contactout.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub ContactOut skill page](https://clawhub.ai/oomol/skills/oo-contactout)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce oo CLI commands and ContactOut connector JSON responses for agent use.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
