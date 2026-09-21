## Description:

Helps an agent deploy static sites to Alibaba Cloud OSS with bucket setup, static hosting, custom domains, HTTPS certificates, GitHub Actions deployment, renewal, and post-deploy verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to publish frontend-only sites from directories such as dist, web, out, or build to Alibaba Cloud OSS, then configure public hosting, custom-domain HTTPS, GitHub Actions secrets or variables, and semantic deployment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make an OSS bucket publicly accessible and change OSS, DNS, and certificate configuration.

Mitigation: Use a dedicated public-only bucket and test subdomain, review the target bucket and domain before execution, and use a least-privilege Alibaba RAM user scoped to the intended bucket.

Risk: GitHub Actions setup can write repository secrets or variables and may reuse a locally available GitHub credential.

Mitigation: Provide an explicit least-privilege GitHub token for the target repository and review any secret or variable names before writing them.

Risk: Certificate material, cloud credentials, or unpublished content could be exposed if stored or uploaded carelessly.

Mitigation: Keep certificate files in a private directory with restrictive permissions, pass Alibaba credentials through environment variables, run the public build step with filters such as --no-inbox, and inspect the upload directory before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/aliyun-oss-static-deploy-skill)
- [Project repository and README](https://github.com/oracis/aliyun-oss-static-deploy-skill)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Python script usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that run bundled scripts to upload files, change OSS bucket settings, configure DNS or certificates, and write GitHub Actions secrets or variables.]

## Skill Version(s):

1.1.2 (source: server release evidence; artifact files report 1.1.3 and 1.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
