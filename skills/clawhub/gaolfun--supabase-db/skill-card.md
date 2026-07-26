## Description: <br>
Query, insert, update, delete, and call RPC on Supabase PostgREST tables directly from OpenClaw without server-side code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with Supabase PostgREST tables: selecting, filtering, inserting, updating, deleting, batching rows, calling RPC functions, and inspecting schema details. It is suited for agents that need guided database API operations while respecting Supabase Row Level Security policies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Database update, delete, upsert, or side-effecting RPC guidance could affect production data. <br>
Mitigation: Require explicit confirmation before destructive or side-effecting operations, especially against production projects. <br>
Risk: Using privileged Supabase keys can bypass intended access controls. <br>
Mitigation: Use the anon/public key with strict Row Level Security policies and avoid service_role or secret keys in skill parameters. <br>
Risk: RPC functions defined with elevated database permissions may bypass Row Level Security. <br>
Mitigation: Review function definitions and RLS behavior before calling RPC endpoints that can mutate or expose data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gaolfun/skills/supabase-db) <br>
- [Supabase documentation](https://supabase.com/docs) <br>
- [PostgREST API reference](https://postgrest.org/) <br>
- [PostgREST filtering](https://postgrest.org/en/stable/api.html#filtering) <br>
- [Supabase Row Level Security guide](https://supabase.com/docs/guides/auth/row-level-security) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP request examples, JSON response shapes, SQL policy snippets, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Supabase project URL and anon/public key; mutation and side-effecting RPC operations should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
