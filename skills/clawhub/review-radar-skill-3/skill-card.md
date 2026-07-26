## Description: <br>
Review Radar turns Bilibili or YouTube monitor review videos, or manual transcript text, into structured review intelligence cards with test data, pros and cons, reviewer conclusions, competitor mentions, references, timestamps, and validation status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ford828](https://clawhub.ai/user/ford828) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit review video URLs or local transcript text to a Review Radar service, retrieve Markdown or JSON reports, and synthesize consensus and disagreements across multiple monitor reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted video URLs, manual transcript files, and report queries are sent to the configured Review Radar HTTP service. <br>
Mitigation: Use the default local service unless a remote endpoint is trusted, and avoid submitting sensitive URLs, transcripts, or report queries. <br>
Risk: The security summary reports unsafe argument handling in the manual text helper. <br>
Mitigation: Use the manual text helper only with trusted file paths and titles, and avoid sensitive local files. <br>
Risk: Generated reports can contain degraded validation status when multiple references fail verification. <br>
Mitigation: Review citations, timestamps, source type, and validation status before relying on a report or synthesized comparison. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ford828/skills/review-radar-skill-3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, JSON job and report metadata, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include original references, timestamps, validation status, and source type.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
