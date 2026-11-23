## Description:

Deploys static websites to Alibaba Cloud OSS with custom-domain HTTPS, GitHub Actions automation, and certificate renewal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to publish static websites to Alibaba Cloud OSS, configure custom domains and HTTPS, and set up deployment and certificate-renewal workflows.

### Deployment Geography for Use:

Global; Alibaba Cloud regions are configurable, and mainland China custom-domain deployments require ICP filing.

## Known Risks and Mitigations:

Risk: The security scan flags destructive effects during dry runs.

Mitigation: Avoid installation until dry-run behavior has been addressed; verify dry runs issue no cloud write or delete operations.

Risk: The security scan flags unsafe handling of local certificate keys and Git credentials.

Mitigation: Avoid use until local key and credential handling has been reviewed and secured; keep secrets out of logs and source control.

Risk: The security scan flags Function Compute routing changes beyond the stated deployment purpose.

Mitigation: Review any Function Compute routing changes before enabling them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/aliyun-oss-static-deploy-skill)
- [Project homepage listed in manifest](https://github.com/oracis/aliyun-oss-static-deploy-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment scripts, configuration steps, and verification commands.]

## Skill Version(s):

1.1.6 (source: skill frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
