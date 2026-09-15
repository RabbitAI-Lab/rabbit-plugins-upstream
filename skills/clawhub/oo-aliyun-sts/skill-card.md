## Description:

Provides agent access to Alibaba Cloud STS credential operations through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to request Alibaba Cloud STS temporary credentials from a connected OOMOL account after checking the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs credential minting operations while describing the connector broadly as safe read/search behavior.

Mitigation: Confirm the intended STS action, role or federation scope, and payload before execution, and treat returned temporary credentials as sensitive.

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer installing the oo CLI from a verified release or package source before using the connector.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-sts)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Alibaba Cloud RAM and STS](https://www.alibabacloud.com/product/ram)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; temporary credential responses should be treated as sensitive.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
