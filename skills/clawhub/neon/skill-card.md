## Description:

Guides developers in choosing and setting up Neon’s Lakebase Postgres, authentication, object storage, functions, AI Gateway, and realtime services for applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to select Neon backend services for an application and follow setup guidance for database, auth, storage, functions, AI, realtime, and related integrations.

### Deployment Geography for Use:

Global; the skill states that Object Storage, Functions, AI Gateway, and Realtime are available in aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1.

## Known Risks and Mitigations:

Risk: The security review says the skill directs silent diagnostic reporting.

Mitigation: Require approval of the exact diagnostic report before transmission.

Risk: The security review says examples can expose database passwords through database-URL logging.

Mitigation: Remove database-URL logging and keep credentials out of diagnostic output.

Risk: Sensitive uploads, permanent project deletion, and broad MCP access can affect user data or project resources.

Mitigation: Keep sensitive uploads private, require explicit authorization for permanent deletion, and scope MCP access to the intended project and permissions.

Risk: The security review notes that downloaded dependencies and future updates were not reviewed.

Mitigation: Keep skill updates user-controlled and review dependencies or updates before relying on them.

## Reference(s):

- [Neon documentation index](https://neon.com/docs/llms.txt)
- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md)
- [Neon Functions runtime limits](https://neon.com/docs/compute/functions/reference/runtime-limits.md)
- [Authentication guide](references/auth.md)
- [Claimable Neon guide](references/claimable-neon.md)
- [Function triggers guide](references/function-triggers.md)
- [Logs and Loki guide](references/logs-loki.md)
- [Environment parsing guide](references/parse-env.md)
- [Neon SDK guide](references/sdk.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell commands, code examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
