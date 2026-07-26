## Description: <br>
Secrets-safe encrypted OpenClaw backups to S3/R2/B2/MinIO with lean modes, opt-in cron, and staged restore for explicit OpenClaw backup and restore requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[obuchowski](https://clawhub.ai/user/obuchowski) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure, run, verify, schedule, and restore encrypted cloud backups of OpenClaw state to S3-compatible storage after explicit user request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that a plaintext override can bypass encryption for sensitive backup scopes if misused. <br>
Mitigation: Avoid --force-plaintext, require a configured passphrase before full or settings backups, and use config.excludeSecrets=true only when an explicitly plaintext-shareable archive is required. <br>
Risk: Backups may contain OpenClaw configuration, credentials, secret stores, and state that are sensitive if uploaded or restored incorrectly. <br>
Mitigation: Use dry-run and explicit confirmation gates for first uploads, restores, prune operations, configuration writes, and schedule creation; prefer staged restores before any in-place overwrite. <br>
Risk: Plaintext credentials stored in OpenClaw config can be copied into every archive that includes openclaw.json. <br>
Mitigation: Store S3 credentials in an AWS profile or operator-managed environment and store the GPG passphrase in a chmod-600 file or OpenClaw SecretRef. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/obuchowski/skills/cloud-backup) <br>
- [Publisher profile](https://clawhub.ai/user/obuchowski) <br>
- [Project homepage](https://github.com/obuchowski/openclaw-cloud-backup) <br>
- [Credentials](references/credentials.md) <br>
- [Setup flow](references/setup-flow.md) <br>
- [Security](references/security.md) <br>
- [AWS S3 provider guide](references/providers/aws-s3.md) <br>
- [Cloudflare R2 provider guide](references/providers/cloudflare-r2.md) <br>
- [Backblaze B2 provider guide](references/providers/backblaze-b2.md) <br>
- [DigitalOcean Spaces provider guide](references/providers/digitalocean-spaces.md) <br>
- [MinIO provider guide](references/providers/minio.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke a bundled shell script for backup, verification, restore, prune, status, setup, and schedule workflows.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release evidence and CHANGELOG.md, released 2026-07-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
