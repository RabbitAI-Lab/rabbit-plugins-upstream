## Description:

Pendo (pendo.io). Use this skill for Pendo requests involving searching and reading data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Pendo connector schemas and run read-oriented Pendo actions for features, pages, and integration status through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may lead an agent or user to execute unverified remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a verified package, signed release, or manually reviewed installer before using the skill.

Risk: Authentication and Pendo connection setup can attach this skill to a real Pendo account.

Mitigation: Run authentication or connection steps only after intentionally deciding to connect the skill to that Pendo account.

## Reference(s):

- [ClawHub Pendo skill](https://clawhub.ai/oomol/skills/oo-pendo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pendo homepage](https://www.pendo.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI connector commands and guidance to inspect live action schemas before execution.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
