## Description:

Waterfall helps agents inspect live Waterfall action schemas and run OOMOL oo CLI connector actions for enrichment, account usage, job-change, and email-verification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Waterfall through an OOMOL-connected account, including launching and retrieving enrichment jobs, checking job changes, verifying email deliverability, and reviewing account usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill under-labels remote enrichment job launches as safe reads.

Mitigation: Confirm the exact company or contact payload, intended effect, and any quota or billing impact before running enrichment launch actions.

Risk: The security review says the skill recommends unverified remote installer execution.

Mitigation: Prefer a verified package source or inspect the installer before using direct shell or PowerShell installer pipelines.

## Reference(s):

- [Waterfall homepage](https://www.waterfall.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waterfall)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and a connected Waterfall account; live action schemas should be inspected before submitting JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
