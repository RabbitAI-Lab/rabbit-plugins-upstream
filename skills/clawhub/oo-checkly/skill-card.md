## Description:

Operate Checkly through an OOMOL-connected account to retrieve checks, check results, statuses, and account details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Checkly monitoring data through an OOMOL-connected account. It supports reading checks, statuses, results, and account details using live connector schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include live remote installer commands that could execute unverified code if run automatically.

Mitigation: Install the oo CLI through a trusted, verified method and do not allow the agent to run curl-to-shell or PowerShell remote installer commands automatically.

Risk: Future or added connector actions that change Checkly state could affect monitoring configuration or data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before any write or destructive action is run.

## Reference(s):

- [ClawHub Checkly skill](https://clawhub.ai/oomol/skills/oo-checkly)
- [Checkly homepage](https://www.checklyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credentials are supplied server-side by OOMOL; the agent should not handle raw Checkly tokens.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
