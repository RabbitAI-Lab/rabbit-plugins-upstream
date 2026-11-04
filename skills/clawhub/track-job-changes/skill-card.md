## Description:

Checks existing contacts for job changes and reports their new role or company when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams use this skill to check a curated set of existing CRM contacts for job changes and identify updated company or title information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job-change checks use contact data and charge 3 credits per contact, so large batches can consume credits quickly.

Mitigation: Use only contacts you are authorized to share, sample 10–20 records first, and confirm the batch size and estimated cost before a full run.

Risk: Setup installs the global CLI using an unpinned package version.

Mitigation: Review the package and version selected for installation before running setup.

Risk: The optional full Cargo pack and its linked recipe were not audited with this release.

Mitigation: Review that installation and recipe separately before use.

Risk: Optional GitHub starring requires access to the user's account.

Mitigation: Only star the repository after the user gives explicit consent.

## Reference(s):

- [ClawHub release](https://clawhub.ai/cargo-ai/skills/track-job-changes)
- [Cargo GTM Skills project homepage](https://github.com/getcargohq/gtm-skills)
- [Job change monitoring recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [JSON data, Text]

**Output Format:** [Per-contact results with a job_change_status and updated person details for movers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One result per contact; the documented action costs 3 credits per contact.]

## Skill Version(s):

1.1.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
