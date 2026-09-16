## Description:

Enables agents to operate Beehiiv through an OOMOL-connected account for reading, creating, and updating Beehiiv data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Beehiiv connector schemas and run Beehiiv actions through OOMOL-managed credentials for publications, posts, and subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-step remote installer commands can execute unreviewed code.

Mitigation: Use a reviewed, versioned, and verified installation path for the oo CLI, and do not let an agent run curl-to-bash or PowerShell installer commands automatically.

Risk: Beehiiv requests and responses route through OOMOL-managed services.

Mitigation: Install only if this routing is acceptable for the Beehiiv data involved, and avoid sending data outside the intended Beehiiv workflow.

Risk: Connector actions can change Beehiiv data when the action is write-capable or destructive.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Beehiiv Skill Page](https://clawhub.ai/oomol/skills/oo-beehiiv)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Beehiiv Homepage](https://www.beehiiv.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when run through the oo CLI; the skill directs agents to inspect live schemas before constructing payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
