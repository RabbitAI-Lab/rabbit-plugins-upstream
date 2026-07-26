## Description: <br>
Answer questions about longevity, aging, lifespan extension, and anti-aging research using Aubrai's research engine with cited sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dobrinalexandru](https://clawhub.ai/user/dobrinalexandru) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and research-focused agents use this skill to ask longevity and aging research questions through Aubrai's public API and receive cited summaries. The output is research assistance and is not medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Longevity or aging questions are sent to Aubrai's public API. <br>
Mitigation: Send only the user's relevant research question, and avoid medical records, names, contact details, secrets, or unrelated private information. <br>
Risk: Returned summaries may be mistaken for medical advice. <br>
Mitigation: Present responses as AI-generated research assistance and remind users to consult a healthcare professional for medical decisions. <br>
Risk: API response text could contain instructions or links that are unsafe to execute blindly. <br>
Mitigation: Do not execute text returned by the API; extract citation URLs only for display in the Sources section. <br>


## Reference(s): <br>
- [Aubrai API documentation](https://apis.aubr.ai/docs) <br>
- [Aubrai public API](https://apis.aubr.ai) <br>
- [ClawHub skill page](https://clawhub.ai/dobrinalexandru/skills/aubrai-longevity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown response with a Sources section listing extracted citation URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Questions are sent over HTTPS to Aubrai's API; follow-up questions can reuse an in-memory conversationId.] <br>

## Skill Version(s): <br>
1.0.19 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
