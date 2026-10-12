## Description:

Looks up details for up to 10 TikTok videos by video ID to help assess engagement and commerce performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketers query TikTok video details to review playback, engagement, and product-sales performance across up to 10 video IDs at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs automatic installation or upgrade of unpinned local Node/npm tooling and persistent environment changes.

Mitigation: Use a preinstalled, pinned qhkit version; require explicit approval before package installation, upgrades, or PATH changes.

Risk: Configuring a Qinghu API token can store credentials locally.

Mitigation: Require explicit approval before token storage and handle the token as a secret.

Risk: Video-detail lookups consume paid Qinghu credits, with actual charges varying by results returned.

Mitigation: Estimate the charge and obtain user consent before paid calls; report actual credit usage afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; tabular file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 video IDs per lookup; paid Qinghu credits may apply.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
