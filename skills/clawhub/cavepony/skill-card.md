## Description: <br>
Cavepony provides pony-themed token compression and expansion for AI agent responses, with lite, full, ultra, pony, and canterlot modes plus a CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrismcfee](https://clawhub.ai/user/chrismcfee) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use Cavepony to make AI responses or agent memory files more concise while preserving technical substance and selected code-like content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional auto-activation hooks can persistently change agent response style across sessions. <br>
Mitigation: Use CLI-only text compression unless persistent response changes are intended; review the generated hook file and remove it from the hooks directory to stop automatic activation. <br>
Risk: File compression overwrites the target file after creating a backup. <br>
Mitigation: Run file compression on copies or under version control, and review the original backup before committing changes. <br>
Risk: Destructive compression modes remove words or substitute one-way terms that cannot be fully expanded back to the original text. <br>
Mitigation: Use lite mode or keep the original text when round-trip fidelity matters. <br>


## Reference(s): <br>
- [Cavepony ClawHub skill page](https://clawhub.ai/chrismcfee/skills/cavepony) <br>
- [Cavepony publisher profile](https://clawhub.ai/user/chrismcfee) <br>
- [Cavepony project repository](https://github.com/cavepony/cavepony) <br>
- [Caveman compression project](https://github.com/JuliusBrussee/caveman) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Compressed or expanded natural-language text, with code blocks, URLs, file paths, and commands intended to remain unchanged.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Modes include lite, full, ultra, pony, and canterlot; destructive compression modes are not fully reversible.] <br>

## Skill Version(s): <br>
0.3.0 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
