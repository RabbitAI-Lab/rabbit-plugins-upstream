## Description: <br>
Retrieves Zhihuiya (PatSnap) patent claim data for one patent by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
IP professionals, patent analysts, R&D teams, and agent developers use this skill to fetch and present the claims section for a single patent. It supports claim-count review, independent or dependent claim display, and optional related-family substitution when claims are unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores full API responses locally, and saved responses may include patent claim data and request metadata. <br>
Mitigation: Review the saved LinkFox response directory before sharing or committing workspace files, and control the execution directory when handling sensitive patent work. <br>
Risk: The skill can consume paid LinkFox/Zhihuiya credits and is limited to one patent per request. <br>
Mitigation: Confirm the target patent and expected credit usage before repeated calls, especially for multiple-patent workflows. <br>
Risk: The skill includes feedback submission and onboarding/install behavior that can involve additional network calls. <br>
Mitigation: Disable or control feedback and onboarding flows unless the user explicitly accepts those extra network and installation behaviors. <br>


## Reference(s): <br>
- [Zhihuiya Claim Data API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, API calls, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses, saved response files, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, queries one patent per call, uses a 24-hour local cache, and may summarize large responses while saving the full JSON response.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
