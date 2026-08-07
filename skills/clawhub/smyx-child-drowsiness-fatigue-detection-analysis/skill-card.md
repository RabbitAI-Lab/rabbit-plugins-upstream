## Description: <br>
Analyzes classroom or home-desk child face videos to estimate drowsiness from PERCLOS, nodding, eye-region changes, and return a 0-100 fatigue index with rest guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers, parents, and education technology operators use this skill to assess child fatigue in classroom, home-desk, or online-class videos. It returns visual fatigue metrics, a structured fatigue assessment, rest reminders, and report links without providing a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends children's video files or video URLs to the publisher's remote service for analysis. <br>
Mitigation: Use only with guardian consent, process only media the user is authorized to submit, and avoid sending unnecessary or sensitive recordings. <br>
Risk: The skill can create or reuse a local identity and maintain token-backed account state. <br>
Mitigation: Run it in a controlled environment, review local account and token storage, and clear local state when it is no longer needed. <br>
Risk: The skill can retrieve cloud report history associated with the resolved identity. <br>
Mitigation: Use accounts scoped to the intended child or classroom context and restrict access to users authorized to view those reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown or JSON structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fatigue metrics, fatigue score and level, drowsiness events, voice prompt text, summary text, and report links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
