## Description: <br>
Manage Cloudflare Workers, KV, D1, R2, and secrets using the Wrangler CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asleep123](https://clawhub.ai/user/asleep123) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to deploy and manage Cloudflare Workers and related Cloudflare resources with Wrangler. It provides command references, configuration examples, troubleshooting notes, and boundaries for tasks Wrangler does not manage directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wrangler commands can delete, roll back, migrate, or bulk-change Cloudflare resources. <br>
Mitigation: Verify the Cloudflare account, environment, resource names, and production impact before running destructive or bulk commands. <br>
Risk: D1 SQL, migration, and bulk operations can alter or remove application data. <br>
Mitigation: Export or back up data before delete, migration, SQL, rollback, or bulk operations. <br>
Risk: Secret commands can expose credentials if plaintext values are stored in shell history, logs, committed files, or shared terminals. <br>
Mitigation: Use interactive secret entry where possible and avoid writing plaintext secrets to history, logs, repositories, or shared terminal sessions. <br>


## Reference(s): <br>
- [Wrangler Docs](https://developers.cloudflare.com/workers/wrangler/) <br>
- [Workers Docs](https://developers.cloudflare.com/workers/) <br>
- [D1 Docs](https://developers.cloudflare.com/d1/) <br>
- [R2 Docs](https://developers.cloudflare.com/r2/) <br>
- [KV Docs](https://developers.cloudflare.com/kv/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Cloudflare Wrangler command references, JSONC and TOML configuration examples, troubleshooting guidance, and operational cautions.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
