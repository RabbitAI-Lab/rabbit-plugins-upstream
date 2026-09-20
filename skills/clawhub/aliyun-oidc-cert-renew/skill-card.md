## Description:

用 GitHub Actions 和阿里云 RAM OIDC 自动续期 Let's Encrypt 通配证书，并分发到 OSS、FC 和 CDN，帮助仓库避免保存长期 AK。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to configure keyless GitHub Actions access to Aliyun, renew wildcard certificates with ACME DNS-01, and distribute certificates across Aliyun services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aliyun RAM trust rules and policies may grant broader cloud access than required.

Mitigation: Narrow OIDC subject matching, actions, and resources to the specific repositories, buckets, domains, functions, and certificate APIs needed before use.

Risk: Credential-access guidance involving ~/.git-credentials may expose GitHub tokens if copied without review.

Mitigation: Avoid that guidance and use approved GitHub authentication flows or short-lived tokens.

Risk: Certificate deletion and distribution steps can affect production HTTPS endpoints.

Mitigation: Back up state, review planned targets, and test with a manual workflow dispatch before scheduled rollout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/aliyun-oidc-cert-renew)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML, Bash, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup and workflow guidance for cloud credentials, certificate renewal, and certificate distribution.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
