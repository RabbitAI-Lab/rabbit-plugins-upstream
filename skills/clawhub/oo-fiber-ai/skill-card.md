## Description:

Fiber AI (fiber.ai). Use this skill for Fiber AI requests that search or read data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to query Fiber AI account and reference information through an OOMOL-connected account. It covers read-only organization credit, rate-limit, and enum/reference dataset actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can lead to running remote installer scripts when the oo CLI is missing.

Mitigation: Install and verify the oo CLI manually through a trusted process before using the skill.

Risk: The skill depends on OOMOL-mediated Fiber AI account access.

Mitigation: Use only approved OOMOL account connections and inspect live action schemas before running connector actions.

## Reference(s):

- [Fiber AI homepage](https://fiber.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Fiber AI skill listing](https://clawhub.ai/oomol/skills/oo-fiber-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
