## Description:

Helps agents work with Guandata BI by routing standard tasks to official tools and providing guidance for ETL governance, dashboard troubleshooting, publishing, and data architecture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Guandata BI developers and analysts use this skill to plan and troubleshoot ETL migrations, dataset and metric operations, custom dashboards, and mobile reporting. It also guides an agent using an authenticated Guandata CLI profile for authorized BI tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using an authenticated Guandata CLI profile can access and modify BI resources.

Mitigation: Install only for intended Guandata workspaces and use a least-privileged BI account.

Risk: Delete, overwrite, or bulk migration actions can change or remove BI data and configurations.

Mitigation: Prefer dry-run or preview, review generated plans, and require explicit confirmation before destructive or bulk changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Project homepage (listed in skill metadata)](https://github.com/maojiebc/majia-guanyuan)
- [Official CLI compatibility guide](references/official-cli-compatibility.md)
- [ETL full-chain rewrite guide](references/part-b17-fullchain-rewrite.md)
- [Custom chart playbook](references/custom-chart-playbook.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BI migration plans, SQL, and dashboard implementation guidance.]

## Skill Version(s):

3.2.3 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
