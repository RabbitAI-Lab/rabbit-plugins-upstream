## Description:

Helps an agent deploy static sites to Aliyun OSS with custom domains, HTTPS certificates, GitHub Actions deployment, and certificate renewal guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to guide OSS bucket setup, static site upload, domain binding, HTTPS certificate issuance or reuse, GitHub Actions configuration, and renewal checks for Aliyun-hosted static sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide changes to public access, DNS records, certificates, Function Compute domains, and GitHub repository settings.

Mitigation: Review each proposed cloud or repository change before execution, and test first with a dedicated Aliyun RAM user and test bucket.

Risk: The GitHub helper may use local GitHub credentials when an explicit token is not provided.

Mitigation: Set a narrowly scoped GITHUB_TOKEN explicitly and do not allow the helper to read ~/.git-credentials.

Risk: Certificate helpers may persist TLS private keys locally.

Mitigation: Store generated certificate keys under a protected account or adjust filesystem permissions before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/aliyun-oss-static-deploy-skill)
- [Source repository](https://github.com/oracis/aliyun-oss-static-deploy-skill)
- [Publisher profile](https://clawhub.ai/user/oracis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment checks, troubleshooting steps, and credential-handling guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
