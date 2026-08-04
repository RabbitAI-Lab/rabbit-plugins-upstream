## Description: <br>
hybrids3 helps agents and developers use a self-hosted object store through S3-compatible, plain HTTP, and MCP interfaces for object upload, download, listing, deletion, and presigned URL workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and external agent users use this skill to move files through a trusted hybrids3 instance, generate scoped presigned upload or download URLs, and connect agents to object storage over MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public buckets can expose stored objects to anyone who can reach the service. <br>
Mitigation: Use private buckets for sensitive data and keep the service bound to localhost or behind an authenticated reverse proxy unless public access is intentional. <br>
Risk: Bucket keys, master keys, and live presigned URLs are bearer credentials. <br>
Mitigation: Keep keys out of shared prompts and logs, prefer per-bucket keys over the master key, and share presigned URLs only for the intended object and time window. <br>
Risk: Delete operations and presigned PUT overwrite flows can irreversibly remove or replace objects. <br>
Mitigation: Require explicit user confirmation for the exact bucket and key before deletion or overwrite, and avoid enumerate-then-bulk-delete workflows. <br>


## Reference(s): <br>
- [hybrids3 ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/hybrids3) <br>
- [hybrids3 Project Homepage](https://github.com/psyb0t/docker-hybrids3) <br>
- [Setup Reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, JSON examples, API examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May emit object-storage API calls, MCP tool-call guidance, and helper-script commands; destructive actions require explicit bucket and key confirmation.] <br>

## Skill Version(s): <br>
0.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
