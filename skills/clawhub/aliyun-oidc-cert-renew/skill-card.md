## Description:

Guides automated Let's Encrypt wildcard certificate renewal and distribution to Alibaba Cloud OSS, Function Compute, and CDN using GitHub Actions and short-lived OIDC credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to configure GitHub Actions and Alibaba Cloud RAM OIDC for keyless certificate renewal, cloud distribution, and HTTPS onboarding of new subdomains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Alibaba Cloud permissions could grant more access than certificate renewal requires.

Mitigation: Replace wildcard permissions with only the required actions and resource ARNs.

Risk: Wildcard GitHub OIDC owner and repository matching could trust unintended workflows.

Mitigation: Use exact GitHub OIDC subject conditions where possible and verify the intended repository and branch.

Risk: Reading GitHub tokens from local credential storage could expose sensitive credentials.

Mitigation: Do not scrape ~/.git-credentials; use an explicit authenticated GitHub flow instead.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oracis/skills/aliyun-oidc-cert-renew)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell, Python, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OIDC setup and temporary credential helper scripts.]

## Skill Version(s):

1.0.4 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
