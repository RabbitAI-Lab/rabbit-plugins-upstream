## Description:

Guides art creation, technique development, and appreciation with practical, medium-specific advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill for art creation guidance, technique development, and art appreciation across media such as drawing, sculpture, and photography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and command execution authority that is not clearly required for art-advice functionality.

Mitigation: Use it only in a constrained environment or narrow and remove unnecessary permissions before installation.

Risk: The artifact includes API-key setup guidance even though the art-advice workflow does not clearly require external API access.

Mitigation: Rely on the host agent's secret handling, avoid hard-coded credentials, and omit API access unless a reviewed deployment explicitly needs it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/art)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown text with optional JSON-shaped examples and shell configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured scoring, recommendations, improvements, or troubleshooting guidance.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
