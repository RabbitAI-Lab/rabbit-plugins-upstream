## Description:

Helps agents preview, configure, and manage scheduled alerts for Cargo workspace workflows, storage models, and queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to monitor workflow failures, spending, latency, model freshness, and custom query results, then review alert history and adjust thresholds or actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alert actions can create paid or externally visible runs on repeated breaches.

Mitigation: Preview the alert, set an appropriate threshold and schedule, and review actions before enabling it.

Risk: The CLI requires Cargo credentials and can change alerts in the active workspace.

Mitigation: Confirm the active workspace with cargo-ai whoami and use the narrowest token with the necessary observability permissions.

Risk: Installing @cargo-ai/cli@latest does not pin the CLI version.

Mitigation: Prefer a pinned CLI version when possible.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo observability release](https://clawhub.ai/cargo-ai/skills/cargo-observability)
- [Alert lifecycle](references/alert-lifecycle.md)
- [Scopes and thresholds](references/scopes-and-thresholds.md)
- [Alert recipes](references/examples/recipes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash commands and JSON alert configurations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses are JSON; alerts can trigger scheduled actions.]

## Skill Version(s):

1.1.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
