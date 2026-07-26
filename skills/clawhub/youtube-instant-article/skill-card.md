## Description: <br>
Transforms YouTube videos into Telegraph Instant View articles with visual slides and timestamped summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[viticci](https://clawhub.ai/user/viticci) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to turn YouTube videos into shareable Telegraph Instant View articles for Telegram, with extracted slides, timestamped summaries, and source video links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ordinary YouTube summary requests may send video-derived text and images to third-party services and publish the resulting article publicly. <br>
Mitigation: Use this skill only when public Telegraph publishing is intended, and avoid processing private, sensitive, or restricted videos. <br>
Risk: The skill loads local environment files for credentials. <br>
Mitigation: Use dedicated least-privilege Telegraph and OpenAI credentials, and avoid sourcing broad environment files. <br>
Risk: The release security verdict is suspicious because the advertised publishing behavior can expose derived content outside the local agent environment. <br>
Mitigation: Review the generated article and destination services before deployment, and treat uploaded images and published pages as publicly accessible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/viticci/skills/youtube-instant-article) <br>
- [summarize CLI](https://github.com/steipete/summarize) <br>
- [Telegraph API](https://telegra.ph/api) <br>
- [catbox.moe](https://catbox.moe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands] <br>
**Output Format:** [Telegraph article URL plus generated article content with timestamped sections and image embeds] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Publishes article content to Telegraph and uploads extracted slides to third-party image hosting.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
