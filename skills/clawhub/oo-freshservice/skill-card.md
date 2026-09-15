## Description:

Freshservice enables an agent to read Freshservice data and create tickets or service requests through OOMOL's Freshservice connector and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and IT operators use this skill to list and retrieve Freshservice tickets, locations, and service catalog items, and to create tickets or service requests from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer one-liners for installing the oo CLI.

Mitigation: Do not let an agent run those installer commands automatically; install the CLI through a trusted, reviewed, versioned process before using the skill.

Risk: Write actions can create Freshservice tickets or service requests.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Freshservice skill page](https://clawhub.ai/oomol/skills/oo-freshservice)
- [Freshservice homepage](https://www.freshworks.com/freshservice/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
