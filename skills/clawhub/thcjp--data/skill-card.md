## Description:

数据 helps agents extract, clean, analyze, and visualize batch data, with Chinese-language interaction and support for data-processing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to prepare, analyze, summarize, and visualize batch data. It is not positioned for real-time streaming data processing or complex decisions requiring human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, glob, and shell execution authority for data workflows.

Mitigation: Install only in a scoped workspace, review generated commands before approval, and limit file access to intended datasets.

Risk: Data provided to the agent may include sensitive or proprietary information.

Mitigation: Use only data approved for the agent environment and redact secrets, credentials, and regulated personal data before processing.

Risk: The artifact claims security controls such as encryption and command whitelisting that the release evidence does not show as enforced.

Mitigation: Treat those claims as unverified and rely on platform-level controls, sandboxing, and independent review before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/data)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON data-processing guidance, with optional code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data summaries, processing steps, visualization guidance, and execution logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
