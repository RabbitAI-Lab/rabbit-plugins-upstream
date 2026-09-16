## Description:

Operate Rollbar through an OOMOL-connected account using the oo CLI to read, create, and update Rollbar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Rollbar projects, items, occurrences, deploys, environments, and item occurrence history through an OOMOL-connected Rollbar account. They can also prepare connector payloads after checking the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the setup instructions for using unverified remote installer scripts.

Mitigation: Review installation steps before installing and use a trusted, verified method for the oo CLI.

Risk: Some Rollbar actions may change Rollbar state when run with constructed payloads.

Mitigation: Inspect the live schema first and confirm any state-changing payload and expected effect before execution.

## Reference(s):

- [ClawHub Rollbar skill page](https://clawhub.ai/oomol/skills/oo-rollbar)
- [Rollbar homepage](https://rollbar.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action payloads should be built only after inspecting the live connector schema.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
