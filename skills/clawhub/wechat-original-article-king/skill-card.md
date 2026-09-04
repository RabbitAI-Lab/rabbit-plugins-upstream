## Description:

Provides daily WeChat Official Account original viral article rankings, category/date filtering, Markdown article tables, subscription prompts, and HTML report generation through RedFox data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, WeChat editors, content planners, and operations teams use this skill to retrieve original WeChat article rankings, compare category trends, review date-specific lists, and create shareable HTML/PDF reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and sends query category/date data to redfox.hk.

Mitigation: Configure the key as an environment variable, confirm its scope and revocation path before use, and avoid exposing it in code, prompts, logs, or generated files.

Risk: The fetch behavior disables HTTPS certificate checks while using the API key.

Mitigation: Review and fix certificate verification or explicitly accept the transport risk before installing or running the skill.

Risk: Generated HTML reports load remote executable JavaScript for PDF export.

Mitigation: Treat generated reports as network-dependent and review remote-script use before opening or sharing reports in sensitive environments.

Risk: Article data is saved locally as JSON and HTML report artifacts.

Mitigation: Handle generated files according to local retention, sharing, and cleanup expectations.

## Reference(s):

- [Category mapping reference](references/category_mapping.md)
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-original-article-king)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox article ranking API endpoint](https://redfox.hk/story/api/cozeSkill/getWxDataByCategoryAndTime)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown article tables with generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; outputs are data snapshots and may include locally saved JSON/HTML artifacts.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
