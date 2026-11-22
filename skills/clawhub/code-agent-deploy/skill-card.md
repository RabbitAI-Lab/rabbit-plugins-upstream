## Description:

Deploys local web projects and backend APIs through a platform, handling readiness checks, packaging, retries, status reporting, logs, and rollback without requiring the user to manage a server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ppjsw2014](https://clawhub.ai/user/ppjsw2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to prepare and deploy local websites, web applications, and backend APIs through the deployment platform. It guides deployment setup, safety checks, status reporting, log review, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags destructive application-deletion and broader administrative commands beyond the stated deployment purpose, and the review is incomplete.

Mitigation: Review deletion and administrative actions before use, and verify which permissions the host grants.

Risk: The security review reports a provisional Next.js dependency advisory.

Mitigation: Verify the advisory and affected Next.js version before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ppjsw2014/skills/code-agent-deploy)
- [appcli reference](references/appcli-reference.md)
- [Stack conventions](references/stacks.md)
- [Base images](references/base-images.md)
- [Personal project configuration](references/personal-configuration.md)
- [Next.js and SQLite example](references/example-nextjs-sqlite/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands, configuration examples, code diffs, and deployment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific; may include deployment changes, status, logs, and rollback guidance.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
