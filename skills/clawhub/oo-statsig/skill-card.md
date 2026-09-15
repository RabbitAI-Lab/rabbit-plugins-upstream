## Description:

Use this skill to read Statsig projects, feature gates, dynamic configs, and segments through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Statsig project data, feature gates, dynamic configs, and segments from an agent session without handling raw Statsig credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Statsig read requests and responses are routed through OOMOL.

Mitigation: Install and use the skill only when that routing is acceptable for the workspace, and confirm the connected Statsig scopes before use.

Risk: The setup guidance includes remote installer commands.

Mitigation: Prefer a verified, signed, or package-manager installation path for the oo CLI before running connector commands.

## Reference(s):

- [Statsig homepage](https://www.statsig.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-statsig)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector output summaries and setup recovery guidance.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
