## Description:

Sanitize log entries by removing passwords, tokens, API keys, and other sensitive patterns using local Expanso Edge pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aronchick](https://clawhub.ai/user/aronchick)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to sanitize log lines or log files before sharing, publishing, or forwarding them to log aggregation and support workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP mode exposes an unauthenticated HTTP endpoint and can bind on all interfaces.

Mitigation: Use CLI mode when possible, or bind the MCP service to localhost and place authentication and request limits in front of any network exposure.

Risk: The redaction rules can miss JSON, quoted, multiline, or unusual credential formats.

Mitigation: Treat the output as best-effort sanitization and review sensitive logs before sharing or forwarding them.

Risk: The skill processes secret-bearing log content.

Mitigation: Run it in a controlled local environment and limit retained inputs, outputs, and operational logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aronchick/skills/expanso-log-sanitize)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration]

**Output Format:** [JSON responses and Markdown usage guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs sanitized text, redaction counts, matched-pattern metadata, trace identifiers, timestamps, and mode-specific metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
