## Description:

Linux DO lets agents search and read Linux DO public topics, posts, tags, categories, groups, users, badges, and trending content through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to answer Linux DO requests by inspecting live action schemas and fetching public forum data through OOMOL's linux_do connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Install oo only from a trusted, verified, versioned release or package manager, or inspect the installer before execution.

Risk: Linux DO requests can encounter private resources, rate limits, authentication failures, CLI errors, or billing stops.

Mitigation: Inspect the live action schema before requests, handle 404, 429, authentication, CLI, and HTTP 402 errors distinctly, and avoid treating inaccessible resources as definitely nonexistent.

## Reference(s):

- [ClawHub Linux DO skill page](https://clawhub.ai/oomol/skills/oo-linux-do)
- [Linux DO homepage](https://linux.do)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Linux DO connector responses returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
