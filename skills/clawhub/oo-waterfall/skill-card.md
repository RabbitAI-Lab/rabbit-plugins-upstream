## Description:

Waterfall enables an agent to use an OOMOL-connected account to inspect and run Waterfall connector actions for enrichment jobs, job-change checks, email verification, and account usage.

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

Risk: The skill is not limited to passive lookups and can launch enrichment or verification actions.

Mitigation: Require explicit user confirmation for action payloads and effects before running launch, verification, or other operational commands.

Risk: The first-time setup section includes remote installer pipelines.

Mitigation: Avoid running remote installer commands unless the installer source has been independently trusted and verified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-waterfall)
- [Waterfall Homepage](https://www.waterfall.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
