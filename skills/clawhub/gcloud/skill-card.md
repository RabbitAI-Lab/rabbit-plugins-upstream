## Description: <br>
Manage Google Cloud Platform resources via gcloud CLI, including Compute Engine VMs, Cloud Run services, Firebase Hosting, Cloud Storage, and project management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jortega0033](https://clawhub.ai/user/jortega0033) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and cloud operators use this skill to get command guidance for operating Google Cloud resources through local gcloud, gsutil, and Firebase CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud commands may change production resources, billing settings, deployments, or databases. <br>
Mitigation: Use least-privileged credentials, verify the active account and project, and require explicit approval before deletes, rollbacks, billing changes, database restores, or production deployments. <br>
Risk: Some commands can expose data or secrets, including public bucket access and Secret Manager reads. <br>
Mitigation: Confirm access intent before public access changes or secret reads, and avoid displaying secret values unless required for the task. <br>
Risk: Generated command guidance can target the wrong Google Cloud project or region if configuration is stale. <br>
Mitigation: Check gcloud configuration and require explicit project, region, and resource identifiers before running impactful commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jortega0033/skills/gcloud) <br>
- [Google Cloud CLI download](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz) <br>
- [Cloud SQL Auth Proxy documentation](https://cloud.google.com/sql/docs/mysql/sql-proxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command-reference guidance for local cloud CLI use; execution requires user credentials and confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
