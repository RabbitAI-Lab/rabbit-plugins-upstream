## Description: <br>
Twinify helps agents create consent-based AI digital twin profiles from WhatsApp chat exports by parsing message history and generating OpenClaw agent profile files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neobotjan2026](https://clawhub.ai/user/neobotjan2026) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Twinify to process a WhatsApp chat export, analyze a consenting person's message style, and generate files needed to create an OpenClaw AI twin for personal or testing contexts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes private WhatsApp chats and may persist parsed data and generated profiles locally. <br>
Mitigation: Use it only with informed consent from the modeled person and affected chat participants, redact private details, keep generated files private, and avoid retaining non-target messages. <br>
Risk: The generated agent template can support deceptive impersonation because it instructs the twin to deny being an AI or assistant. <br>
Mitigation: Revise generated agent instructions so the agent clearly identifies as an AI simulation and prohibit deception, harassment, or impersonation use. <br>
Risk: Consent can be withdrawn after a twin is created. <br>
Mitigation: Delete parsed data, profile files, workspace files, and configuration entries when the modeled person or affected participants withdraw consent. <br>


## Reference(s): <br>
- [Twinify ClawHub listing](https://clawhub.ai/neobotjan2026/skills/twinify) <br>
- [AGENTS.md Template](references/agents-guide.md) <br>
- [SOUL.md Generation Guide](references/soul-guide.md) <br>
- [EXAMPLES.md Generation Guide](references/examples-guide.md) <br>
- [ANTI-EXAMPLES.md Generation Guide](references/anti-examples-guide.md) <br>
- [MEMORY.md Generation Guide](references/memory-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands plus generated JSON and profile files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local parsed chat data and OpenClaw profile/configuration artifacts; no token cap is specified.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
