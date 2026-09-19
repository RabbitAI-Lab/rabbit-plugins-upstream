## Description:

YoPlanning (yoplanning.com). Use this skill for ANY YoPlanning request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read YoPlanning teams, online products, bookable availability slots, and related details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that execute external code.

Mitigation: Install only if OOMOL and the oo CLI installer source are trusted; inspect the installer or use an official verified package path before running it.

Risk: The connected YoPlanning account may expose accessible team, product, and availability data to agent-driven reads.

Mitigation: Connect only the YoPlanning account data intended for agent access and review connector scope or credential errors before retrying.

## Reference(s):

- [YoPlanning homepage](https://www.yoplanning.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return YoPlanning data through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
