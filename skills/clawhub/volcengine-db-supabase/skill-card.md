## Description: <br>
Manages Volcengine's AI-native BaaS platform Supabase edition / AIDAP for workspace, branch, compute, database, Auth, Realtime, Edge Function, Storage, static-site hosting, API key, connection, and TypeScript type tasks through byted-supabase-cli. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to administer Volcengine Supabase / AIDAP resources, run database and schema operations, configure application integration, and troubleshoot access, security, and deployment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Volcengine Supabase resources, including raw SQL changes and stop, delete, deployment, and key-management operations. <br>
Mitigation: Require explicit user intent for state-changing commands, confirm destructive workspace actions, prefer non-production branches first, and run a read-only verification command after changes. <br>
Risk: Credentials, API keys, service-role keys, and persistent CLI profiles can expose administrative access. <br>
Mitigation: Use temporary or least-privilege credentials, avoid shared machines with persistent profiles, do not expose service-role keys to client code, and avoid printing full secret values unless the user explicitly requests them. <br>
Risk: Disabling JWT verification or misconfiguring RLS/Auth policies can weaken application authorization. <br>
Mitigation: Use --no-verify-jwt only for functions with their own authentication or webhook signature checks, enable RLS for exposed tables, and review Auth, RLS, and Storage policies before production use. <br>


## Reference(s): <br>
- [Volcengine](https://www.volcengine.com/) <br>
- [Volcengine AIDAP Changelog](https://www.volcengine.com/docs/87275/2105759?lang=zh) <br>
- [Volcengine Database Documentation](https://www.volcengine.com/docs/87275/2385100?lang=zh) <br>
- [Volcengine Authentication Documentation](https://www.volcengine.com/docs/87275/2277072?lang=zh) <br>
- [Volcengine Realtime Documentation](https://www.volcengine.com/docs/87275/2277058?lang=zh) <br>
- [Volcengine Edge Function Documentation](https://www.volcengine.com/docs/87275/2288709?lang=zh) <br>
- [Application Integration Guide](references/app-integration-guide.md) <br>
- [Command Reference for byted-supabase-cli](references/tool-reference.md) <br>
- [Security Checklist](references/security-guide.md) <br>
- [Row Level Security Guide](references/rls-guide.md) <br>
- [Schema Design and Migration Guide](references/schema-guide.md) <br>
- [SQL Playbook](references/sql-playbook.md) <br>
- [AIDAP Deploy Database Provider](references/deploy-provider.md) <br>
- [Postgres Performance and Best Practices](references/pg-best-practices/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, SQL, JSON snippets, and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Volcengine CLI commands, SQL migrations, application configuration, and verification steps for the invoking agent to run with appropriate credentials.] <br>

## Skill Version(s): <br>
2.3.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
