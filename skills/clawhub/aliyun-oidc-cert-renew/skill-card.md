## Description:

Automates Let's Encrypt wildcard certificate renewal and distribution to Alibaba Cloud services through GitHub Actions and RAM OIDC without storing long-term access keys in the repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

Developers and DevOps engineers use this skill to configure GitHub Actions and Alibaba Cloud RAM OIDC for recurring certificate renewal, ACME DNS-01 issuance, CAS upload, and OSS/FC/CDN distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default cloud permissions may grant broad Alibaba Cloud access.

Mitigation: Narrow RAM policies to the exact APIs and resources required before installation.

Risk: Broad GitHub OIDC trust patterns can allow more workflow subjects than intended.

Mitigation: Replace wildcard OIDC subjects with exact allowed subjects where possible.

Risk: Temporary STS credentials exported to the workflow environment can be used by later workflow steps.

Mitigation: Run only trusted workflow steps after credentials are written and pin dependencies used by the automation.

## Reference(s):

- [Server-resolved source repository](https://github.com/oracis/aliyun-oidc-cert-renew)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, YAML, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational setup steps and review guidance for cloud credential scope.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
