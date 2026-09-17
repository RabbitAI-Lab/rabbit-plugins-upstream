## Description:

Operate cloudlayer.io through an OOMOL-connected account to create PDF jobs, inspect jobs and assets, and check account usage with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to perform cloudlayer.io account, PDF generation, job, and asset workflows through an OOMOL-connected oo CLI session without handling raw API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI only from a trusted source, preferably with a pinned version and verified checksum or signature.

Risk: PDF job creation actions change cloudlayer.io account state and may consume account credits.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [cloudlayer.io homepage](https://cloudlayer.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected cloudlayer.io account; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
