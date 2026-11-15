## Description:

Retrieves timestamped YouTube transcripts through okdata so agents can summarize, quote, and compare videos in the requested language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

People researching video content can use the skill to retrieve timestamped transcripts, then request summaries, notes, key points, chapters, quotations with time links, or comparisons across videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains an example for retrieving Weibo trends that does not match its described video transcript purpose.

Mitigation: Review that example and confirm its purpose before running it; use the transcript workflow only when that is the intended task.

Risk: The supplied security scan is incomplete, so its benign verdict does not establish that every aspect of the skill was assessed.

Mitigation: Review the skill before installation and decide whether its behavior and API key use are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-transcripts)
- [okdata YouTube transcript API](https://okdata.online/apis/youtube/videos/transcript/get/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, notes, quotations, and comparisons with timestamp links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript language can be original or selected; outputs preserve timestamps and attribute claims to the speaker.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
