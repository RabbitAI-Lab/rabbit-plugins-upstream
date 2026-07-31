## Description: <br>
hybrids3 helps agents and developers work with a self-hosted object store through S3-compatible, plain HTTP, and MCP interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use hybrids3 to upload, download, list, delete, and presign objects in a self-hosted S3-compatible object store over S3, plain HTTP, or MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured hybrids3 endpoint can expose public buckets, bearer keys, presigned URLs, deletes, and object overwrites. <br>
Mitigation: Install only for trusted endpoints, keep sensitive objects in private buckets, use per-bucket keys instead of the master key, and avoid sharing live credentials or presigned URLs in prompts or logs. <br>
Risk: Delete operations and presigned PUT overwrites are destructive and irreversible. <br>
Mitigation: Require explicit user confirmation for the exact bucket and key before deleting or overwriting an object, and avoid enumerate-then-bulk-delete workflows. <br>
Risk: Binding the service to a public interface can make buckets and APIs reachable from the network. <br>
Mitigation: Bind to loopback or a protected internal network unless remote access is deliberate, and place production access behind an appropriate reverse proxy or network control. <br>


## Reference(s): <br>
- [hybrids3 setup](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/hybrids3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include object-storage operation guidance, curl commands, MCP configuration, boto3 examples, and JSON responses.] <br>

## Skill Version(s): <br>
0.3.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
