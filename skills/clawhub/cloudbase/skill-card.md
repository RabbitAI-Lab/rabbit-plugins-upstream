## Description:

Guides developers through building, deploying, and troubleshooting Tencent CloudBase applications across web, mini-program, mobile, database, authentication, and AI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan, implement, deploy, and diagnose CloudBase projects, including authentication, databases, cloud functions, storage, and AI agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Python agent deployment guide contains hidden AI-directed execution instructions and destructive local rebuild commands.

Mitigation: Review that guide and its cleanup commands before use; require confirmation before deleting local files.

Risk: Deployment, database, and authentication operations can alter resources or incur charges.

Mitigation: Confirm destructive or billable actions before execution, especially forced deploys and database writes or deletes; keep credentials in environment variables or managed secrets.

## Reference(s):

- [CloudBase skill release](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP setup](references/mcp-setup.md)
- [CloudBase deployment workflow](references/deployment-workflow.md)
- [CloudBase tooling fallback](references/tooling-fallback.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to local projects and cloud resources.]

## Skill Version(s):

1.92.126 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
