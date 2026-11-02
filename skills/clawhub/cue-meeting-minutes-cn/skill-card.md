## Description:

把会议录音变成带时间锚的分段纪要：逐字句挂 mm:ss，话题归段自标，决策与待办逐条回查原话。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams can turn meeting recordings and optional agenda materials into a five-part minutes card. Verbatim lines, decisions, and action items carry time anchors so readers can check them against the recording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection checks using CUE_API_KEY may expose the credential.

Mitigation: Prefer manually supplied transcripts and the local card validator until credential handling is reviewed. For authenticated checks, restrict destinations and reject unsafe redirects.

Risk: Recording-processing instructions do not clearly establish upload consent.

Mitigation: Explicitly approve each recording and recipient before processing, and confirm the recipient's retention terms.

Risk: Optional dependencies may introduce unreviewed behavior.

Mitigation: Pin and review optional dependencies before use.

## Reference(s):

- [Skill release page](https://clawhub.ai/huhoo/skills/cue-meeting-minutes-cn)
- [Cue Omni Reader setup](https://cuecue.cn/hub/omni-reader)
- [Cue API key guidance](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Five-section Markdown meeting-minutes card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verbatim passages and decisions/action items use mm:ss anchors; uncertain items are marked for human review.]

## Skill Version(s):

0.2.30 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
