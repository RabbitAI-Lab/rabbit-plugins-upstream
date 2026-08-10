## Description:

Mesh app factory guides agents through building, configuring, deploying, and operating MeshServer end-to-cloud business applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyinmind](https://clawhub.ai/user/flyinmind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create MeshServer services with service, database, API, UI, authorization, deployment, and operations guidance. It is suited to resource-constrained end-to-cloud business application development and includes example services for inventory, CRM, finance, HR, user management, workflow, and related business workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or modified service configs, SQL, role checks, and backup settings can affect real business, financial, or operational data.

Mitigation: Review service configuration, database changes, SQL statements, role checks, and backup settings before using the results with production data.

Risk: Default or administrative credentials may be present in setup examples or deployment flows.

Mitigation: Change default/admin credentials during setup and verify authentication and authorization behavior before exposing services to users or networks.

Risk: External downloads and ecosystem-specific dependencies can introduce operational or supply-chain risk.

Mitigation: Install only when intending to use the MeshServer ecosystem, verify download sources, and scan artifacts before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyinmind/skills/mesh-app-factory)
- [MeshServer homepage](https://gitee.com/zhijian_net/MeshServer)
- [MeshServer services](https://gitee.com/zhijian_net/enterprise)
- [Inventory example README](artifact/examples/inventory/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, configuration, code, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce service definitions, database definitions, API configuration, UI implementation guidance, deployment steps, and review recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
