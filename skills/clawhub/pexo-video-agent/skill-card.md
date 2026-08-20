## Description:

Pexo Video Agent helps agents create finished multi-shot AI videos from text, images, URLs, scripts, or audio through Pexo's external video-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pexo](https://clawhub.ai/user/pexo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to turn natural-language briefs, selected media, product URLs, scripts, or audio into finished short-form and marketing videos while the agent manages project setup, uploads, status polling, billing confirmations, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User briefs, selected media files, and project metadata are sent to Pexo for video generation.

Mitigation: Obtain explicit user consent before the first external transmission and upload only files the user selected for the video task.

Risk: The PEXO_API_KEY grants authenticated access to the user's Pexo account.

Mitigation: Keep the key private, store it in ~/.pexo/config with restrictive permissions or an environment variable, and rotate it if it is exposed.

Risk: Billable video-generation batches can consume Pexo credits.

Mitigation: Review the available credit estimate and require explicit user approval before confirming any billable batch.

Risk: Generated videos and fetched media may remain in the local cache.

Mitigation: Periodically delete cached media from ~/.pexo/tmp or PEXO_TMP_DIR when outputs are sensitive.

## Reference(s):

- [Setup Checklist](references/SETUP-CHECKLIST.md)
- [Troubleshooting](references/TROUBLESHOOTING.md)
- [Pexo OpenClaw Guide](https://pexo.ai/connect/openclaw)
- [ClawHub Skill Page](https://clawhub.ai/pexo/skills/pexo-video-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON command outputs, plain URLs, and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PEXO_API_KEY, bash, curl, jq, file, outbound HTTPS to https://pexo.ai, and local cache storage under ~/.pexo/tmp or PEXO_TMP_DIR.]

## Skill Version(s):

0.3.16 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
