## Description: <br>
Use TokenLab native endpoint families such as Responses, Anthropic Messages, Gemini generateContent, media, audio, embeddings, and translations when OpenAI-compatible chat is not the right contract. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hedging8563](https://clawhub.ai/user/hedging8563) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose TokenLab native endpoints, preserve provider-specific request semantics, and recover from endpoint hints or contract errors when OpenAI-compatible chat is not appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, files, or API keys used with generated TokenLab request examples may be shared with the TokenLab service. <br>
Mitigation: Use this skill only when routing through TokenLab is intended, and avoid sending secrets or private content unless the TokenLab account and applicable policies allow it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hedging8563/skills/tokenlab-native-endpoints) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with a runnable code or cURL block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes the chosen endpoint, a minimal request example, a short fit explanation, and a recovery note.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
