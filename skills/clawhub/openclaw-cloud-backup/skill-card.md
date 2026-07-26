## Description: <br>
Secrets-safe encrypted OpenClaw backups to S3/R2/B2/MinIO, with lean modes, opt-in cron, staged restore, and activation only for explicit OpenClaw backup or restore requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[obuchowski](https://clawhub.ai/user/obuchowski) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure, run, verify, restore, prune, and schedule encrypted OpenClaw state backups to S3-compatible storage when explicitly requested. It helps coordinate provider setup, least-privilege credentials, dry runs, confirmation gates, and restore safety. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive full or settings backups could be uploaded as plaintext if the plaintext escape hatch is used or encryption is not configured. <br>
Mitigation: Do not use --force-plaintext for full or settings backups; configure a passphrase file before cloud upload and verify encryption during the dry run. <br>
Risk: Cloud credentials or backup passphrases can be exposed if stored in OpenClaw config or shared in the conversation. <br>
Mitigation: Use least-privilege bucket-scoped credentials in an AWS profile or operator-managed environment, and store the backup passphrase in a chmod-600 file or SecretRef entered outside the conversation. <br>
Risk: Restore, prune, and retention actions can overwrite state or delete backup history. <br>
Mitigation: Run dry runs first, show the exact file or deletion plan, prefer staged restores, and require explicit confirmation before each high-impact action. <br>
Risk: Scheduled backups could run without clear operator intent. <br>
Mitigation: Offer scheduling only after a successful manual backup, print the exact cron command, and create or change schedules only after explicit opt-in. <br>


## Reference(s): <br>
- [Source homepage](https://github.com/obuchowski/openclaw-cloud-backup) <br>
- [ClawHub skill page](https://clawhub.ai/obuchowski/skills/openclaw-cloud-backup) <br>
- [Setup flow](references/setup-flow.md) <br>
- [Credential handling](references/credentials.md) <br>
- [Security threat model](references/security.md) <br>
- [AWS S3 provider guide](references/providers/aws-s3.md) <br>
- [Cloudflare R2 provider guide](references/providers/cloudflare-r2.md) <br>
- [Backblaze B2 provider guide](references/providers/backblaze-b2.md) <br>
- [DigitalOcean Spaces provider guide](references/providers/digitalocean-spaces.md) <br>
- [MinIO provider guide](references/providers/minio.md) <br>
- [Other S3-compatible providers](references/providers/other.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command output to relay to the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create encrypted backup archives, cloud uploads, restore plans, prune plans, and configuration changes only after the skill's explicit request and confirmation gates.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
