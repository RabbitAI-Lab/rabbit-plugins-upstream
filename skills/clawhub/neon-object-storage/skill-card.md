## Description: <br>
S3-compatible object storage that branches with your Neon project, so files and the database stay in sync across every branch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add branch-aware object storage to Neon/Lakebase applications, including bucket setup, S3-compatible clients, upload/download flows, and presigned URLs. <br>

### Deployment Geography for Use: <br>
United States (us-east-2 Neon region) <br>

## Known Risks and Mitigations: <br>
Risk: Generated AWS_* values and branch environment files can expose Neon storage credentials if committed, logged, or used in client-side code. <br>
Mitigation: Keep .env files out of source control and logs, avoid exposing credentials to client-side code, and rotate credentials if they are shared accidentally. <br>
Risk: Neon Object Storage is described as a public beta available only for new projects in us-east-2. <br>
Mitigation: Confirm the Neon project is new and in us-east-2 before provisioning buckets or wiring application code. <br>


## Reference(s): <br>
- [Neon parent skill source](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Neon Object Storage overview](https://neon.com/docs/storage/overview.md) <br>
- [Neon Object Storage get started](https://neon.com/docs/storage/get-started.md) <br>
- [Neon Object Storage buckets](https://neon.com/docs/storage/buckets.md) <br>
- [Neon Object Storage objects](https://neon.com/docs/storage/objects.md) <br>
- [Neon Object Storage authentication](https://neon.com/docs/storage/authentication.md) <br>
- [Neon S3 compatibility](https://neon.com/docs/storage/s3-compatibility.md) <br>
- [Neon Object Storage troubleshooting](https://neon.com/docs/storage/troubleshooting.md) <br>
- [Files SDK docs](https://files-sdk.dev) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with TypeScript and shell command code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include environment variable names and S3 client configuration; treats AWS_* credential values as secrets.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
