## Description:

Debug settings that work in one execution path but vanish in another by tracing config resolution through every runtime entry point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to debug runtime configuration settings that persist but do not propagate across entry points or modes. It guides them through effective-config checks, source tracing, focused tests, and live verification before declaring success.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Effective configuration, status surfaces, or runtime logs may include provider names, model choices, or environment-specific details.

Mitigation: Review and redact sensitive configuration and log excerpts before sharing them, and inspect any proposed source or test change before applying it.

Risk: A fix may address one execution path while leaving an alternate mode or resolver path with stale or missing configuration.

Mitigation: Require focused resolver tests, live effective-config confirmation, a real request through the affected entry point, and downstream log evidence before declaring success.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional inline commands and code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces debugging steps, verification criteria, and risk-aware recommendations; no external tool calls are required by the skill itself.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
