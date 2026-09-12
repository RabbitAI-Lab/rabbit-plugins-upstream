## Description:

Writes or audits README files against the Standard Readme specification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and documentation maintainers use this skill to create, rewrite, or audit project README files for Standard Readme compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to read normal project files while writing or auditing a README, which can expose unrelated private material in sensitive repositories.

Mitigation: Use it within the intended repository scope and avoid exposing secrets or unrelated private files to the agent.

Risk: Generated README content can include inaccurate commands, links, or license statements if the available project evidence is incomplete.

Mitigation: Review proposed README content against the project files before publishing.

## Reference(s):

- [Standard Readme specification](https://github.com/RichardLitt/standard-readme)
- [standard-readme skill homepage](https://github.com/tenequm/skills/tree/main/skills/standard-readme)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/standard-readme)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code, Shell commands]

**Output Format:** [Markdown documents or concise audit findings, often with fenced code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or rewrite README.md, or report ordered README audit findings without rewriting]

## Skill Version(s):

0.1.5 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
