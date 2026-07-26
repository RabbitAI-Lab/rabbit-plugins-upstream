## Description: <br>
WorkOS (workos.com). Use this skill for ANY WorkOS request: reading, creating, updating, and deleting WorkOS data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage WorkOS organizations, AuthKit users, and organization memberships from an agent session. It supports read actions for account data and confirmed write actions for creating, updating, reactivating, and deactivating WorkOS resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects WorkOS account data to OOMOL through the oo CLI. <br>
Mitigation: Install only when OOMOL's oo CLI and credential handling are trusted, and treat read actions as account-data access. <br>
Risk: Write and destructive actions can create, update, reactivate, or deactivate WorkOS organizations, users, and memberships. <br>
Mitigation: Review the live action schema and exact JSON payload, then get explicit user confirmation before running state-changing or destructive actions. <br>
Risk: A missing, expired, or under-scoped WorkOS connection can cause commands to fail or request reconnection. <br>
Mitigation: Run setup or reconnection steps only after an auth, connection, scope, or credential error indicates they are needed. <br>


## Reference(s): <br>
- [WorkOS homepage](https://workos.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub WorkOS skill page](https://clawhub.ai/oomol/skills/oo-workos) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI, including connector data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
