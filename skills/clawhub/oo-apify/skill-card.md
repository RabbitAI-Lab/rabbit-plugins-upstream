## Description:

Apify (apify.com). Use this skill for ANY Apify request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Apify through an OOMOL-connected account, including reading actor, user, dataset, and run data and starting actor runs after confirming payloads and side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start Apify actor runs that may change account state or create costs.

Mitigation: Require confirmation of run_actor payloads, expected effects, and potential costs before execution.

Risk: The documented first-time setup includes remote installer pipelines.

Mitigation: Verify the oo CLI source and version independently before running installer commands.

Risk: Apify actions and data are routed through OOMOL-connected infrastructure.

Mitigation: Install only when the user accepts routing Apify activity through OOMOL and avoid sending sensitive data unless appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apify)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Apify homepage](https://apify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON action results from Apify through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
