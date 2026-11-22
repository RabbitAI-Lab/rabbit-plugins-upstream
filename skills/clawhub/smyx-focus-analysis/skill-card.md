## Description:

Real-time detection of gaze direction and facial pose to quantify states of focus, distraction, or mind-wandering. Suitable for scenarios such as classroom learning, office meetings, and driving attention monitoring. | 专注度分析技能，实时检测视线方向、面部姿态，量化专注/分心/走神状态，适用于课堂学习、办公会议、驾驶专注度监测等场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, meeting organizers, and safety staff use the skill to analyze video for gaze direction, head pose, focus, and distraction, then review a structured analysis report or historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags credential handling, remote requests, and video-upload behavior that are not yet explained; the review is incomplete because a referenced local path was missing.

Mitigation: Before installation, establish the account and credential flow, confirm the remote destinations and video-upload behavior, and review the missing reference; avoid installation until these are understood.

## Reference(s):

- [Skill API reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files]

**Output Format:** [JSON analysis results by default, with optional Markdown summaries and report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focus scores, distraction statistics, trend summaries, recommendations, report links, or a saved output file.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
