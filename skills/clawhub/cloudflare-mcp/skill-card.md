## Description: <br>
Uses Cloudflare Code Mode MCP to let an agent call Cloudflare APIs for Workers, DNS, R2, D1, KV, Vectorize, and other Cloudflare endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Cloudflare operators use this skill to ask an agent to inspect and manage Cloudflare resources such as Workers, DNS records, KV namespaces, R2 buckets, D1 databases, and account information through MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad OAuth-backed ability to change live Cloudflare resources. <br>
Mitigation: Use the narrowest OAuth permissions available, prefer a test account or limited zone, and revoke the Cloudflare OAuth grant when finished. <br>
Risk: DNS, Workers, storage, or account changes may affect production services if executed without review. <br>
Mitigation: Require explicit confirmation before DNS, Workers, storage, or account changes. <br>


## Reference(s): <br>
- [Cloudflare MCP homepage](https://github.com/cloudflare/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/2233admin/cloudflare-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and natural-language task prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Cloudflare MCP search() and execute() tools after OAuth authorization.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
