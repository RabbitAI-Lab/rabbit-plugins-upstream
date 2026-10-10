## Description:

Installs and tests free LLM endpoints in WorkBuddy, with options to verify tool calling and monitor availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users can configure no-key LLM services, test whether the configured models work with agent tools, and watch for outages or rate limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests to third-party free LLM services may expose sensitive content.

Mitigation: Do not send secrets, private user data, or production code to these endpoints.

Risk: Installation, refresh, or removal changes local model configuration.

Mitigation: Use --dry-run to review changes first and retain the configuration backup.

Risk: Watch mode makes repeated requests and free endpoints can become rate-limited or unavailable.

Mitigation: Use a bounded watch interval or round count, stop monitoring when unnecessary, and verify availability before relying on a model.

## Reference(s):

- [Free LLM Installer on ClawHub](https://clawhub.ai/oracis/skills/free-llm-installer)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Status reports]

**Output Format:** [Markdown with inline shell commands and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the installer can update local model configuration and create backups, logs, and watch state.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
