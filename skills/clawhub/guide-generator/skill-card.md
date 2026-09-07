## Description:

Generates practical lifestyle guides by researching Chinese social platforms and official sources, cross-checking recommendations, and turning the findings into ready-to-use Markdown guides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhs1r](https://clawhub.ai/user/zhs1r)

### License/Terms of Use:

MIT-0

## Use Case:

External users and lifestyle content creators use this skill to produce travel, food, shopping, sports, and outdoor activity guides with cross-validated recommendations, prices, routes, alternatives, safety notes, and source summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may perform broad web research and produce outdated or misleading guide details.

Mitigation: Cross-check recommendations against independent sources and official sources, include negative feedback, and keep the information-validity date visible in each guide.

Risk: The skill may use local PowerShell curl for WeChat links.

Mitigation: Prefer removing shell fetching or tightly allowlisting it before install, and review any command before execution.

Risk: The skill can save generated guides to a local path.

Mitigation: Confirm the destination path with the user before writing files and avoid overwriting existing work without explicit approval.

## Reference(s):

- [Output Templates](references/output_templates.md)
- [ClawHub Skill Page](https://clawhub.ai/zhs1r/skills/guide-generator)
- [Publisher Profile](https://clawhub.ai/user/zhs1r)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown guide with tables, source notes, validity date, and optional saved .md file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide body targets 2000-3500 Chinese characters excluding tables and checklists; outdoor topics include safety notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
