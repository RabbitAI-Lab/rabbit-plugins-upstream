## Description: <br>
Architects, debugs, secures, and cost-optimizes Google Cloud deployments across Cloud Run, GKE, Compute Engine, BigQuery, Cloud SQL, IAM, VPC, Vertex AI, Pub/Sub/Dataflow, backups, infrastructure as code, and gcloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to plan, operate, debug, secure, and cost-optimize Google Cloud projects. It supports service selection, IAM and networking diagnosis, billing analysis, production readiness, gcloud command guidance, and Terraform-oriented infrastructure decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains persistent local Google Cloud memory across ~/Clawic/data/gcp/ and shared server, domain, contact, and project files, which may contain sensitive operational metadata. <br>
Mitigation: Review the configured local paths before use, keep file permissions appropriate for infrastructure metadata, and store credential pointers rather than credential values. <br>
Risk: The skill can propose operational Google Cloud changes, including destructive actions such as deleting projects or datasets, destroying key versions, detaching billing, or removing node pools. <br>
Mitigation: Require an explicit confirmation step and blast-radius review before any destructive command, and keep destructive commands out of copy-paste blocks of read-only commands. <br>
Risk: The skill depends on local gcloud, user credentials, Application Default Credentials, or impersonated service accounts, so commands can run against the wrong account or project if context is stale. <br>
Mitigation: Verify the active account, project, region, and impersonation target before execution, and prefer least-privilege identities for operational commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/gcp) <br>
- [Clawic Google Cloud Skill](https://clawic.com/skills/gcp) <br>
- [Security Guidance](artifact/security.md) <br>
- [gcloud Commands and Safety](artifact/commands.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, configuration snippets, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce gcloud commands, Terraform-oriented infrastructure guidance, and local Clawic memory updates; destructive operations should be separated from read-only commands and require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
