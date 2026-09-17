## Description:

Helps agents search and read Alibaba Cloud Simple Log Service projects, logstores, logs, and histograms through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Alibaba Cloud SLS resources and query log data through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation includes remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Prefer a verifiable package source, or inspect and verify the installer before execution.

Risk: Queried SLS log data may contain personal data, secrets, or regulated information and is routed through OOMOL as a third-party connector.

Mitigation: Review the OOMOL trust boundary before installation and query only log data the user is authorized to access.

## Reference(s):

- [ClawHub Alibaba Cloud SLS Skill Page](https://clawhub.ai/oomol/skills/oo-aliyun-sls)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Alibaba Cloud Simple Log Service](https://www.alibabacloud.com/product/log-service)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema checks and read-only connector run commands.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
