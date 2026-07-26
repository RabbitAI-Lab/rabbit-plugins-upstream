## Description: <br>
Generates condensed time-lapse album highlight reports from local or URL videos by extracting segments that match user-specified keywords or targets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user wants to find and summarize people, pets, scenes, or events in long videos, or retrieve prior time-lapse analysis reports linked to the current account identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send videos, video URLs, and prompts to a cloud analysis service. <br>
Mitigation: Use it only with media that is appropriate for the listed cloud processing behavior, and avoid sensitive personal media unless that handling is acceptable. <br>
Risk: The skill silently creates or reuses an account-like identifier and stores account tokens locally. <br>
Mitigation: Run it in an environment where local account persistence is expected, and clear the skill data store when account linkage should not persist. <br>
Risk: The skill can retrieve account-linked historical reports with limited user control. <br>
Mitigation: Review history-query requests before use and avoid sharing the resulting report list or links outside the intended account context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown report text with embedded JSON and report links; optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report history and export links; detail can be basic, standard, or json.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter declares 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
