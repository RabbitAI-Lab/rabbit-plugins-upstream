## Description:

Tencent VOD Intl. helps agents generate Python commands for Tencent Cloud VOD uploads, media processing, AIGC media generation, metadata queries, search, token management, and task or sub-application workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud media operators use this skill to turn Tencent Cloud VOD requests into executable Python CLI commands for upload, processing, AIGC generation, querying, search, and token workflows. It is intended for users who already have authority to operate the target Tencent Cloud account and media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated commands can submit billable Tencent Cloud VOD processing or AIGC jobs.

Mitigation: Use dry-run first, require explicit confirmation before processing commands, and configure budget alerts or spending caps for the Tencent Cloud account.

Risk: Commands may upload media, query account metadata, or process confidential or biometric content in Tencent Cloud.

Mitigation: Run the skill only for media the user is authorized to process and avoid sending sensitive content unless the account, region, and data handling requirements are approved.

Risk: The scripts can load cloud credentials from dotenv files and save AIGC tokens locally.

Mitigation: Use a dedicated dotenv file with least-privilege Tencent Cloud credentials, restrict file permissions, and rotate tokens when no longer needed.

Risk: The scripts can auto-install or upgrade Python packages in the execution environment.

Mitigation: Run in a trusted, isolated Python environment and review dependency changes before using the skill on production systems.

## Reference(s):

- [Tencent VOD Intl. ClawHub release page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod-intl)
- [Tencent Cloud VOD pricing](https://cloud.tencent.com/document/product/266/2838)
- [Tencent Cloud VOD Apply Upload API](https://cloud.tencent.com/document/api/266/31767)
- [Tencent Cloud VOD Process Media API](https://cloud.tencent.com/document/product/266/33427)
- [Tencent Cloud VOD Describe Media Infos API](https://cloud.tencent.com/document/product/266/31763)
- [Tencent Cloud VOD CreateAIGCTask Image API](https://cloud.tencent.com/document/product/266/126240)
- [Tencent Cloud VOD CreateAIGCTask Video API](https://cloud.tencent.com/document/product/266/126239)
- [Tencent Cloud VOD AIGC Token Management API](https://cloud.tencent.com/document/api/266/128054)
- [vod_aigc_audio.md](references/vod_aigc_audio.md)
- [vod_process_media.md](references/vod_process_media.md)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Configuration guidance]

**Output Format:** [Plain text commands with Markdown links for returned media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target Python scripts under scripts/ and may include dry-run flags or confirmation prompts for billable processing.]

## Skill Version(s):

1.1.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
