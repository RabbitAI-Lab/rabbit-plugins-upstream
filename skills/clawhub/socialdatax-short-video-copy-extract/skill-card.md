## Description:

Extracts short-video descriptions, spoken transcripts, copy-ready text, concise summaries, and task status from user-supplied public links, share text, content IDs, or existing job IDs for supported platforms through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit or continue read-only transcript jobs for public Xiaohongshu, Douyin, Kuaishou, Weibo, and WeChat Channels videos. It helps turn returned video context and speech transcripts into copy-ready text, concise summaries, or task-status updates without performing account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied video links, share text, content IDs, job IDs, and API-authorized requests are sent to SocialDataX.

Mitigation: Use the skill only for public videos and only when the user is comfortable sharing those inputs with SocialDataX.

Risk: The examples install and run the npm package with @latest, which can change between runs.

Mitigation: Review package trust and update behavior before deployment; pin or approve package versions where your environment requires reproducibility.

Risk: Polling the same video incorrectly can duplicate submissions or treat an unfinished job as a final transcript.

Mitigation: After a job ID is returned, query only that same job until terminal status and deliver final copy only after a succeeded terminal response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-short-video-copy-extract)
- [SocialDataX API key and service page](https://socialdatax.com/ai?from=clawhub)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured transcript, copy, summary, status, and error sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use only returned fields, continue polling until terminal status when possible, and avoid inventing missing video details.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
