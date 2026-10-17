## Description:

Helps developers build, deploy, and troubleshoot Tencent CloudBase applications across web, mini-program, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan, implement, deploy, and diagnose CloudBase apps, including authentication, databases, cloud functions, storage, AI features, and hosting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The deployment reference may encourage unreviewed execution of commands, including repeated force-deletion of a dependency folder.

Mitigation: Review proposed commands before execution and confirm any rm -rf target is only the intended project dependency folder.

Risk: Plugin installation, login, deployment, or deletion can change local setup or CloudBase resources.

Mitigation: Require explicit user confirmation before installs, authentication, deployments, deletions, or the Python agent rebuild flow.

Risk: Generated code or configuration could expose credentials.

Mitigation: Never paste real secrets into generated code or configuration.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase setup and authentication](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)
- [CloudBase feature routing](references/activation-map.yaml)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authorized CloudBase resource changes and deployments.]

## Skill Version(s):

1.92.142 (source: server release metadata; bundled skill frontmatter says 2.35.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
