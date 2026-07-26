## Description: <br>
Azure Voicelive helps developers configure Azure VoiceLive real-time voice agents for function calling, custom voices, telephony audio formats, advanced sessions, and interruption handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to build or configure enterprise voice assistants, customer-service phone bots, and branded voice experiences on Azure VoiceLive. It provides guidance and example code for API integration, function tools, audio formats, credential setup, and session behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External function calls and webhook integrations could affect accounts, orders, or business data. <br>
Mitigation: Restrict callable functions to an allowlist and require human confirmation before actions that change accounts or business records. <br>
Risk: Phone or caller details could be exposed through model context, logs, or downstream tools. <br>
Mitigation: Use least-privilege Azure credentials and avoid sending raw phone numbers or sensitive caller information unless consent and retention controls are in place. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-voicelive) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python and shell code blocks plus JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Azure VoiceLive setup steps, credential configuration, and integration examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
