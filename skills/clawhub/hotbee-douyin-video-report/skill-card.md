## Description:

Generates a local Chinese Douyin video analysis package from a user-provided public video link, including an HTML report, images, comments, transcript files, markdown breakdowns, raw responses, and a run manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

Content analysts, marketers, and agents use this skill to turn a public Douyin video link into a local report package for video breakdown, comment insight, transcript review, and reusable Chinese analysis files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill may consume the user's HotBee key quota while processing public Douyin links.

Mitigation: Confirm the user is comfortable using their HotBee key and quota before running transcript or comment collection.

Risk: Generated reports, raw files, comments, and transcripts may contain public usernames, comments, timestamps, and location labels.

Mitigation: Review generated files before sharing them or committing them to a repository.

## Reference(s):

- [HotBee Analysis Contract](references/hotbee-analysis-contract.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [ClawHub Skill Page](https://clawhub.ai/shanye1402-hash/skills/hotbee-douyin-video-report)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, analysis]

**Output Format:** [Local HTML, Markdown, CSV, JSON, SVG, image files, raw response files, and concise Chinese guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated local package can include report.html, transcript.md, transcript_raw.txt, comments.csv, comments.json, breakdown.md, images, raw API responses, report_data.json, and run_manifest.json.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
