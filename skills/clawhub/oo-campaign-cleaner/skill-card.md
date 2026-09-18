## Description:

Campaign Cleaner helps an agent operate Campaign Cleaner through the OOMOL oo CLI to inspect action schemas, submit email campaign HTML for analysis, retrieve campaign data and reports, check credits, and delete saved campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Campaign Cleaner from an agent. It supports reading saved campaigns, submitting campaign HTML for analysis, retrieving statuses and PDF reports, checking credits, and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct execution of remote installer scripts.

Mitigation: Use reviewed official installation steps, verify the source where possible, and avoid pipe-to-shell installation before setup.

Risk: The skill can submit campaign data and delete saved Campaign Cleaner campaigns.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit user approval before destructive deletion.

Risk: The skill depends on the OOMOL oo CLI, an OOMOL-connected Campaign Cleaner account, and available credits.

Mitigation: Install only when comfortable with the OOMOL CLI and connector, and handle authentication, connection, or billing failures through the documented setup flow.

## Reference(s):

- [Campaign Cleaner homepage](https://campaigncleaner.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Campaign Cleaner on ClawHub](https://clawhub.ai/oomol/skills/oo-campaign-cleaner)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a Campaign Cleaner PDF analysis report as a transit file; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
