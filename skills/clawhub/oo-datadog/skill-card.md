## Description:

Datadog lets agents search, retrieve, and query Datadog metrics and monitors through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Datadog connector schemas, retrieve Datadog metrics and monitor data, query timeseries points, and validate the configured Datadog API key through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can involve executing remote installer scripts from cli.oomol.com.

Mitigation: Review the installer or verified installation documentation and confirm setup before allowing the agent to run installation commands.

## Reference(s):

- [ClawHub Datadog skill](https://clawhub.ai/oomol/skills/oo-datadog)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Datadog homepage](https://www.datadoghq.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect live Datadog connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
