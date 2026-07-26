## Description: <br>
Use when you need your agent to see the world through your LENS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capachow](https://clawhub.ai/user/capachow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use Lens to personalize an OpenClaw agent with persistent identity, value, and writing-style context. The skill can bootstrap local profile files, schedule recurring refinement jobs, distill recent conversation history, and ask calibration questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring background jobs read recent local OpenClaw conversations and build persistent identity and style data in .lens. <br>
Mitigation: Install only when this personalization behavior is intended; review generated cron jobs and .lens files, and remove lens-distillation and lens-interview to stop ongoing processing. <br>
Risk: Sensitive conversation content may be captured in .lens/TRACE.txt or reflected into profile nodes. <br>
Mitigation: Mark sensitive messages with #private, consider setting anonymize to true in .lens/SCOPE.json, and review generated .lens files before relying on them. <br>


## Reference(s): <br>
- [Lens Skill Page](https://clawhub.ai/capachow/skills/lens) <br>
- [Alignment Scales](references/alignment-scales.md) <br>
- [Resolve Protocol](references/resolve-protocol.md) <br>
- [Trinity Definitions](references/trinity-definitions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, cron job configuration, and local profile file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .lens profile files and emit scheduled job configuration for recurring personalization.] <br>

## Skill Version(s): <br>
1.2.3 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
