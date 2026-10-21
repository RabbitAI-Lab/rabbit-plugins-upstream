## Description:

Guides agents through Guandata BI analysis, ETL governance, dashboard validation, and publishing workflows using the official tools and local reference material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

BI analysts, developers, and engineers use this skill to plan and check Guandata queries, ETL changes, dashboards, and publishing, including read-only validation when direct queries are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BI changes such as deletion, publication, saving, importing, replacement, or metric management can affect production data and dashboards.

Mitigation: Review the Guandata CLI permissions and active BI profile, and require explicit approval before these actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Publisher-listed project homepage](https://github.com/maojiebc/majia-guanyuan)
- [Restricted-query guidance](references/restricted-query-playbook.md)
- [Extraction evidence guidance](references/extraction-evidence.md)
- [Dashboard evidence guidance](references/dashboard-evidence.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Text or Markdown with code and commands; local validation reports where requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested BI workflow and the user's tool permissions.]

## Skill Version(s):

3.5.0 (source: ClawHub release, SKILL.md metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
