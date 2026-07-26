## Description: <br>
Translate between English and MoltLang, a compact AI language that cuts token usage by 50-70% for efficient, validated, and error-handled agent communication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonlnheath](https://clawhub.ai/user/jasonlnheath) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to translate English instructions into MoltLang and decode MoltLang back to English for compact agent-to-agent communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential text could be sent to the disclosed public API during translation. <br>
Mitigation: Avoid sending confidential text to the public API unless the operator and privacy practices are trusted. <br>
Risk: Local install options depend on an external package or repository. <br>
Mitigation: Verify the external MoltLang package or repository before installing local code. <br>
Risk: Generated MoltLang may be unsuitable if the translation is invalid or unsupported. <br>
Mitigation: Use the validation and efficiency commands and review translations before relying on them in agent workflows. <br>


## Reference(s): <br>
- [Moltlang Translator ClawHub page](https://clawhub.ai/jasonlnheath/skills/moltlang-skill) <br>
- [MoltLang GitHub repository](https://github.com/jasonlnheath/moltlang) <br>
- [MoltLang public API](https://moltlang.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with plain-text translations and inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can translate in both directions, validate MoltLang, list available tokens, calculate token efficiency, and suggest public API or local pip/npm usage.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
