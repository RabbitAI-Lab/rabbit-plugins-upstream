## Description:

Operates Emailable through the OOMOL-connected oo CLI for account lookup and email verification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Emailable through an OOMOL-connected account, including retrieving account status, verifying individual or batch email addresses, and checking batch jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email verification actions may consume Emailable credits, even when they are presented as ordinary read-style actions.

Mitigation: Confirm the exact payload and expected credit impact before running individual or batch verification.

Risk: The setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Use an already installed oo CLI when available, and run installer commands only after separately trusting and verifying the OOMOL installer source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emailable)
- [Emailable homepage](https://emailable.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
