## Description:

Genderize (genderize.io). Use this skill for ANY Genderize request — searching and reading data. Whenever a task involves Genderize, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call OOMOL's Genderize connector for name-gender prediction, including single-name predictions and batches of up to 10 names with optional country localization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that execute fetched scripts directly in a shell.

Mitigation: Install the oo CLI through a verifiable method and do not allow an agent to run the curl-to-bash or PowerShell iex installer automatically.

Risk: Names and optional country hints are sent through OOMOL's Genderize connector.

Mitigation: Use the skill only when sharing those inputs with OOMOL and Genderize is acceptable for the user or organization.

Risk: Authentication and connector setup can involve account login, API-key connection, or billing recovery steps.

Mitigation: Let the user review and perform login, connection, billing, and recovery actions instead of running them proactively.

## Reference(s):

- [Genderize homepage](https://genderize.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Genderize ClawHub skill page](https://clawhub.ai/oomol/skills/oo-genderize)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas and returns Genderize connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
