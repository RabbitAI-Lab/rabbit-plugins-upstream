## Description:

Helps developers build, deploy, and troubleshoot CloudBase applications across web, WeChat Mini Programs, and mobile platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill for CloudBase application design, authentication, databases, cloud functions, storage, AI features, deployment, and troubleshooting. It is not intended for projects that do not use CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment instructions could cause cloud changes without sufficient user visibility.

Mitigation: Review deployment plans and require explicit approval before changing resources.

Risk: Database or storage policy changes could delete data or expose resources.

Mitigation: Review SQL, RLS, storage policies, deletion, authentication, and public-access changes before execution.

Risk: Agent deployment guidance includes an rm -rf ./env workflow, and paid-plan actions can incur costs.

Mitigation: Confirm the target directory and obtain explicit approval before deletion or paid-plan changes.

## Reference(s):

- [ClawHub CloudBase release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP setup](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed cloud changes require user review before execution.]

## Skill Version(s):

1.92.117 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
