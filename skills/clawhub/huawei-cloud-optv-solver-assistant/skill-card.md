## Description:

Guides agents through Huawei Cloud OptVerse mathematical optimization workflows, from requirements and modeling to data checks, solving, and publishing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations-research practitioners use this skill to guide an agent through OptVerse requirements analysis, model and data validation, optimization, report generation, and asset publishing. Optional steps deploy and test a published model service.

### Deployment Geography for Use:

China (Huawei Cloud cn-north-7 region for OptVerse operations)

## Known Risks and Mitigations:

Risk: Cloud credentials or cached tokens could be exposed on shared machines.

Mitigation: Review credential handling before installation; use a least-privilege account and a non-sensitive project, and avoid shared machines.

Risk: Insecure TLS handling or permissive token storage could expose cloud access.

Mitigation: Fix TLS verification and token storage permissions before production use.

Risk: Downloaded artifacts with unsafe filenames could affect local files.

Mitigation: Sanitize downloaded filenames before production use.

Risk: Automated confirmations, publishing, deployment, or testing could take unintended cloud actions.

Mitigation: Review outputs and require explicit approval; avoid --auto-confirm, --deploy, and --test unless those actions are intended, and make confirmations fail closed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-optv-solver-assistant)
- [OptVerse workflow design](artifact/references/workflow-design.md)
- [OptVerse API reference](artifact/references/api-reference.md)
- [IAM permissions](artifact/references/iam-policies.md)
- [KooCLI installation guide](artifact/references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown guidance and generated model, data, solver, and report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can publish an OptVerse asset and optionally deploy and test its model service.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
