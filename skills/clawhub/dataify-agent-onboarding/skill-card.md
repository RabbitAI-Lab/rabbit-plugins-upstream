## Description:

Set up and verify a first Dataify workflow, then route the user to MCP, local skills, or REST without losing their original task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to configure Dataify credentials, verify account readiness, and choose the smallest suitable access path for a first Dataify-backed task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure during setup.

Mitigation: Do not ask users to paste tokens into chat; provide only shell commands that set DATAIFY_API_TOKEN locally and never print token values.

Risk: Verification can send an authentication check to Dataify using the configured token.

Mitigation: Run verification only when a readiness check is requested, and treat service, balance, rate limit, and credential failures as setup states before continuing the original task.

Risk: Optional diagnostic telemetry may create local event logs.

Mitigation: Keep telemetry disabled unless DATAIFY_TELEMETRY_FILE is set, and record only allowlisted status fields without queries, URLs, outputs, or credentials.

## Reference(s):

- [Access paths](references/access-paths.md)
- [Dataify documentation](https://doc.dataify.com)
- [Dataify support](https://www.dataify.com/)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-agent-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform one Dataify readiness check when verification is requested; optional telemetry writes allowlisted local diagnostic events only when DATAIFY_TELEMETRY_FILE is set.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
