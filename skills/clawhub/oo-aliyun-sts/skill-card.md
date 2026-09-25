## Description:

Operates Alibaba Cloud STS through an OOMOL-connected account using the oo CLI to assume RAM roles and fetch temporary STS credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Alibaba Cloud STS connector schemas and run OOMOL-backed actions that return temporary credentials for role assumption or OIDC federation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can return temporary Alibaba Cloud credentials.

Mitigation: Require user confirmation before actions that return credentials and avoid copying credential values into chat or logs unless needed.

Risk: The setup flow includes remote oo CLI installer commands.

Mitigation: Verify the installer against OOMOL's official installation documentation before running it.

## Reference(s):

- [Alibaba Cloud STS homepage](https://www.alibabacloud.com/product/ram)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-sts)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return temporary cloud credentials through the oo CLI response payload.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
