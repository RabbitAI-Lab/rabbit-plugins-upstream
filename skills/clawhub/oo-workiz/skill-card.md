## Description:

Workiz lets agents search and read Workiz jobs, leads, and team members through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Workiz jobs, leads, and active team members from an already connected Workiz account. It supports read-only lookup and listing workflows with schema-first JSON payload construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad routing language may cause an agent to select this skill whenever Workiz is mentioned, including for sensitive customer or business-data queries.

Mitigation: Confirm the user intends to query Workiz data before running actions that retrieve jobs, leads, or team members.

Risk: Workiz job, lead, and team-member reads can expose customer or business information from the connected account.

Mitigation: Inspect the live action schema, use the narrowest requested filters or identifiers, and avoid retrieving data beyond the user's stated task.

## Reference(s):

- [ClawHub Workiz skill page](https://clawhub.ai/oomol/skills/oo-workiz)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Workiz homepage](https://www.workiz.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workiz get and list actions return JSON data with response metadata when run through the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
