## Description: <br>
Analyzes adult front-facing facial images or short videos to estimate visual fatigue and stress indicators, returning a 0-100 fatigue/stress index with contributing features and directional suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers can use this skill to assess adult facial fatigue or stress indicators from clear face images or short videos for personal status monitoring, workplace wellness displays, smart mirrors, or health-management applications. Results are directional visual assessments and do not replace medical diagnosis or clinical stress evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facial images, videos, derived fatigue/stress reports, and persistent user identifiers are sent to the publisher cloud service. <br>
Mitigation: Use the skill only with explicit consent from the person depicted, avoid unnecessary or third-party face media, and confirm retention and deletion options before deployment. <br>
Risk: The skill may silently create or reuse a persistent user identity for analysis and history lookup. <br>
Mitigation: Separate identities between users, review local identity and token storage, and document how users can clear or rotate the stored identity. <br>
Risk: A face-based fatigue/stress score can be mistaken for a medical or clinical assessment. <br>
Mitigation: Present outputs as directional visual indicators only, preserve the non-diagnostic warning, and advise professional follow-up for persistent high scores or symptoms. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with fatigue/stress score, level, contributing features, suggestions, and optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save results to an output file and may return historical report lists from the publisher cloud service.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter and changelog text state 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
