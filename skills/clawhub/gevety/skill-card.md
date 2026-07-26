## Description: <br>
Accesses Gevety health data such as biomarkers, healthspan scores, biological age, wearable metrics, medications, medical profile, lab reports, health documents, clinical findings, and health content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moclippa](https://clawhub.ai/user/moclippa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to let an agent retrieve and summarize their Gevety account health data, including biomarkers, wearable trends, biological age clocks, medications, health documents, and protocol actions. It is intended for personal health-data review, not diagnosis or medical decision-making. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive health information through a user-provided Gevety API token. <br>
Mitigation: Use a dedicated Gevety API token, keep it out of chat when possible, request only the specific health data needed, and revoke the token when it is no longer needed. <br>
Risk: Health summaries, biomarker trends, and scenario results could be mistaken for medical advice. <br>
Mitigation: Present retrieved data clearly, avoid diagnosis, and direct users to consult qualified healthcare providers for medical decisions. <br>


## Reference(s): <br>
- [Gevety](https://gevety.com) <br>
- [Gevety Skill Page](https://clawhub.ai/moclippa/skills/gevety) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown and structured summaries derived from Gevety API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided GEVETY_API_TOKEN and access to the user's Gevety account data.] <br>

## Skill Version(s): <br>
1.12.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
