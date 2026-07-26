## Description: <br>
Provides patient-facing general health education by matching health topics and keywords to article summaries and source references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to build a general health education entry point that matches a user's topic and keywords to relevant article summaries and source references. It is intended for health education only, not diagnosis or personalized treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health topics, keywords, matched article summaries, and extracted document text may be sent to a remote medical model API. <br>
Mitigation: Avoid real patient identifiers and sensitive medical records unless the publisher provides privacy, retention, and compliance assurances. <br>
Risk: Broad Office, PDF, and image input support may process files that contain unintended sensitive content. <br>
Mitigation: Process uploads only in a controlled environment and review files before submitting them to the skill. <br>
Risk: Generated health education may be mistaken for medical diagnosis or personalized treatment advice. <br>
Mitigation: Keep outputs framed as education, preserve the non-diagnostic disclaimer, and route clinical decisions to qualified medical professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-health-education) <br>
- [WellAlly health skill source reference](https://agent-skills.md/skills/huifer/WellAlly-health/wellally-tech) <br>
- [Hivoice medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [UTF-8 JSON containing structured matched-article data and Markdown text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey for the documented remote medical model API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
