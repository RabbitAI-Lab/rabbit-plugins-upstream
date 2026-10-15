## Description:

Retrieves a TikTok creator's published videos by user ID or unique ID using Qinghu AI data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to look up a TikTok creator's recent videos and review content performance with Qinghu AI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node changes local tooling.

Mitigation: Review and approve installation or upgrades before changing the machine.

Risk: API credentials may be exposed if entered directly into shell commands.

Mitigation: Provide the Qinghu API token through a secure secret mechanism.

Risk: Paid calls may consume more credits as result counts grow.

Mitigation: Confirm estimated costs and user authorization before calling; scope requests to explicit creator video-list lookups.

Risk: Some source instructions describe creator product lists rather than creator videos.

Mitigation: Check the intended video-list tool and its current parameters before making a paid request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-creator-videos)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summaries with optional tabular files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits charged for paid lookups; larger results may be delivered as files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
