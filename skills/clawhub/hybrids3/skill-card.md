## Description: <br>
hybrids3 helps agents and developers use a self-hosted object store through S3-compatible, plain HTTP, and MCP interfaces for uploading, downloading, listing, deleting, and presigning objects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to interact with an already-running hybrids3 object-storage service, manage objects with scoped bucket credentials, generate presigned links, and connect MCP-aware agents to storage workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public buckets are world-readable to anyone who can reach the service. <br>
Mitigation: Keep sensitive data in private buckets and bind the service to loopback or place it behind an authenticated proxy unless remote access is deliberate. <br>
Risk: Bucket keys, master keys, and active presigned URLs are bearer credentials. <br>
Mitigation: Prefer per-bucket keys over the master key, keep credentials out of shared prompts and logs, and limit presigned URLs to the intended object and expiration window. <br>
Risk: Deletes, overwrites, and presigned PUT uploads can irreversibly remove or replace object data. <br>
Mitigation: Require explicit user confirmation for the exact bucket and key before destructive operations, and avoid enumerate-then-bulk-delete workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/hybrids3) <br>
- [hybrids3 homepage](https://github.com/psyb0t/docker-hybrids3) <br>
- [setup.md](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell, Python, JSON, and configuration examples; API and tool calls may return text, JSON, object bytes, or headers.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HYBRIDS3_URL and scoped bucket or master credentials; MCP object downloads are capped at 50 MB.] <br>

## Skill Version(s): <br>
0.3.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
