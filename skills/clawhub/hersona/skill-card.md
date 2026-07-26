## Description: <br>
Hersona applies attribute-based character personas to an agent session, including temporary blends, persistent profiles, recommendations, persona packs, and exports through the hersona CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shiro-0x](https://clawhub.ai/user/shiro-0x) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Hersona to apply, inspect, blend, persist, reset, recommend, and export persona attributes for conversational agents without relying on character-specific data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent mode can intentionally affect future agent sessions. <br>
Mitigation: Use single or multi mode for temporary changes, and use persistent mode only when future sessions should inherit the persona behavior. <br>
Risk: Reset and force-style operations can remove or overwrite persistent persona state. <br>
Mitigation: Check available backups before using reset or --force. <br>
Risk: Persona changes can alter agent tone, role behavior, and prompt content. <br>
Mitigation: Review generated persona blocks and scan the skill before deployment. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/shiro-0x/hersona/tree/main/skills/hersona) <br>
- [Hersona repository](https://github.com/shiro-0x/hersona) <br>
- [ClawHub skill page](https://clawhub.ai/shiro-0x/skills/hersona) <br>
- [Artifact reference](artifact/REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated persona or configuration text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON, message-format, OpenAI Assistants, or LangChain SystemMessage exports when requested.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
