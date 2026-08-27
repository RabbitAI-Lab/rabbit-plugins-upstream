## Description:

本地图表生成引擎 is a local-first chart generation skill that helps agents create bar, line, pie, and scatter visualizations from inline labels and values using Python and matplotlib.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users can use this skill to choose a basic chart type and generate local PNG chart outputs for reports, slides, and quick data review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unexplained API key, callback URL, and API connection instructions that conflict with the skill's offline-only claim.

Mitigation: Review the skill before installation and do not provide API keys, credentials, or callback URLs unless the publisher clarifies why they are needed, where data is sent, and what permissions are required.

Risk: Generated chart files and chart history are retained in local storage and may contain sensitive input data.

Mitigation: Limit access to the local output and history directories, and remove generated files when they include sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chart)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands; generated artifacts are PNG chart files and JSON chart history.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill describes local storage under $HOME/.skill-platform/workspace/memory/chart/ and supports bar, line, pie, and scatter chart outputs.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
