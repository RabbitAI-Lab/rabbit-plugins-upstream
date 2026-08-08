## Description:

AI-powered fruit ripeness grading for tomatoes and strawberries from images or video, returning visual maturity grades, structured analysis, harvest-timing guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, home gardeners, and produce cooperatives use this skill to grade tomato or strawberry ripeness from submitted images, videos, or URLs. The skill helps assess color, colored-area ratio, gloss, relative size, and harvest timing while returning structured reports and historical report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-backed analysis sends local media or submitted URLs to a remote service.

Mitigation: Use only non-sensitive fruit images, videos, or public URLs that are acceptable to upload to the service.

Risk: The skill creates or reuses a service identity and stores account tokens locally.

Mitigation: Run it only in workspaces where local token persistence is acceptable, and review or clear workspace data before sharing the environment.

Risk: Historical report queries retrieve remote report history linked to the resolved service identity.

Mitigation: Avoid using the history feature when report metadata or prior analysis records should not be exposed in the current workspace.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file and may return cloud-hosted report export links.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
