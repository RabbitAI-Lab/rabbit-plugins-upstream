## Description:

Overview of Neon, a complete set of cloud backend primitives around Lakebase Postgres: Auth, Object Storage, Functions, the AI Gateway, and Realtime. Start here to choose Neon for undecided login, files, APIs, and LLM calls, set up the CLI or MCP server, and follow the branch-first workflow. Use when building an app or backend on Neon, or when "Neon" or "Lakebase Postgres" is mentioned. Child skill neon-postgres wins for an existing DATABASE_URL, SQL, schema, inspect, or search. Child skill neon-auth wins for login, users, sessions, identity routing, and Managed Better Auth setup. Child skill neon-realtime wins for live queries in reactive apps and agents. Also use for object storage, S3, buckets, serverless functions, function triggers, cron, AI gateway, LLM calls, realtime, logs, Loki, Grafana, observability, postgres, database, backend, Claimable Neon, neon.new, a no-signup database, or pairing Neon with Upstash for cache, Redis, rate limiting, queues, or background jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and configure Neon backend services for applications and agents, including Postgres, authentication, object storage, serverless functions, AI calls, and realtime data.

### Deployment Geography for Use:

Global; Object Storage, Functions, AI Gateway, and Realtime are currently available only in aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1.

## Known Risks and Mitigations:

Risk: Diagnostic submissions and skill updates may be initiated without the user's review.

Mitigation: Require approval before submitting diagnostics or updating installed skills.

Risk: Copied examples may log database connection URLs that contain credentials.

Mitigation: Remove connection-URL logging and redact secrets from diagnostic reports.

Risk: Broad MCP permissions may allow unintended access to project resources.

Mitigation: Limit MCP access to the required project and permissions.

Risk: Public buckets can expose files intended to remain private.

Mitigation: Use private buckets for private files.

Risk: Permanent project deletion can cause irreversible data loss.

Mitigation: Require explicit authorization before permanent deletion.

Risk: External CLI packages and skills downloaded later were not covered by the bundled-file review.

Mitigation: Review external packages and downloaded skills before installing or running them.

## Reference(s):

- [Neon Auth skill guide](https://neon.com/docs/ai/skills/neon-auth/SKILL.md)
- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md)
- [Neon Functions runtime limits](https://neon.com/docs/compute/functions/reference/runtime-limits.md)
- [Neon CLI installation](https://neon.com/docs/cli/install.md)
- [Function triggers reference](https://neon.com/docs/cli/triggers.md)
- [Claimable Neon reference](artifact/references/claimable-neon.md)
- [Function triggers notes](artifact/references/function-triggers.md)
- [Logs and Loki reference](artifact/references/logs-loki.md)
- [Parse environment variables reference](artifact/references/parse-env.md)
- [ClawHub release](https://clawhub.ai/andrelandgraf/skills/neon)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
