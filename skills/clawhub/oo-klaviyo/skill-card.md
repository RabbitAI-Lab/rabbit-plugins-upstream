## Description:

Klaviyo (klaviyo.com). Use this skill for ANY Klaviyo request: reading, creating, and updating data through the OOMOL-connected Klaviyo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Klaviyo action schemas and operate campaigns, profiles, events, and account metadata through an OOMOL-connected account. It supports read operations and guarded write operations such as creating profile events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review and independently verify the OOMOL installer source before running curl-to-shell or irm-to-iex commands.

Risk: The skill can create Klaviyo profile events through a write action.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-klaviyo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Klaviyo Homepage](https://www.klaviyo.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live Klaviyo connector responses returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
