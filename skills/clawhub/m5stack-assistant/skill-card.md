## Description: <br>
M5Stack Assistant helps agents answer M5Stack product, hardware, software development, compatibility, and troubleshooting questions using official M5Stack MCP knowledge results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuyun2000](https://clawhub.ai/user/yuyun2000) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and support agents use this skill to retrieve official M5Stack product specifications, pinouts, API details, examples, integration guidance, selection comparisons, and troubleshooting information before producing technical answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: M5Stack support questions and feedback may be sent to M5Stack's MCP service and logged there. <br>
Mitigation: Do not include secrets, private customer data, Wi-Fi passwords, tokens, API keys, or other sensitive information in queries or feedback. <br>
Risk: Official M5Stack material may be missing, conflicting, or temporarily unavailable for a specific product or development platform. <br>
Mitigation: State when official material does not confirm an answer, retry with specific product, SKU, platform, interface, or error keywords, and submit reproducible feedback when the documentation gap or issue is confirmed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yuyun2000/skills/m5stack-assistant) <br>
- [M5Stack Official Documentation](https://docs.m5stack.com) <br>
- [M5Stack GitHub](https://github.com/m5stack) <br>
- [Quick Reference](artifact/references/quick-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown answers with optional code blocks, shell commands, configuration snippets, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call M5Stack MCP knowledge_search, knowledge_answer, or knowledge_feedback; queries and feedback may be sent to M5Stack's MCP service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
