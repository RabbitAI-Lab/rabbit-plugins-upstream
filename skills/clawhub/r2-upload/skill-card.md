## Description: <br>
Upload files to Cloudflare R2, AWS S3, or any S3-compatible storage and generate secure presigned download links with configurable expiration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[julianengel](https://clawhub.ai/user/julianengel) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to upload selected local files to Cloudflare R2, AWS S3, MinIO, or other S3-compatible storage, then receive temporary download links, list bucket contents, generate new links, or delete remote objects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload local files selected by the calling agent to a configured cloud bucket. <br>
Mitigation: Install only for trusted agents and use bucket-scoped least-privilege R2/S3 credentials. <br>
Risk: Cloud credentials are required for operation and could expose storage if mishandled. <br>
Mitigation: Keep ~/.r2-upload.yml private, avoid committing configuration files, and rotate credentials if compromise is suspected. <br>
Risk: Delete requests remove the specified remote object immediately. <br>
Mitigation: Review delete requests carefully before allowing the agent to execute them. <br>
Risk: Public URLs, long-lived links, large uploads, or unrestricted file types can increase exposure, storage cost, or misuse risk. <br>
Mitigation: Prefer short presigned URL expirations, avoid public URLs unless intended, monitor file sizes and storage usage, and apply stricter file handling policies where needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/julianengel/skills/r2-upload) <br>
- [README.md](artifact/README.md) <br>
- [CLAWDHUB.md](artifact/CLAWDHUB.md) <br>
- [SECURITY.md](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown-compatible text containing upload status, bucket and object identifiers, presigned URLs, listings, deletion confirmations, and setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Presigned URLs use configurable expiration with a five-minute default; public URL output is available only when explicitly requested and configured.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
