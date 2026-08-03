## Description: <br>
Uydi Voice enables an AI agent to design custom voices, clone authorized voice samples, synthesize narration, manage voices, check credits, and review synthesis history through the Uydi voice platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvyinchao](https://clawhub.ai/user/lvyinchao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to authenticate with Uydi, create or clone permitted voices, synthesize WAV narration, and manage voice assets, credits, and synthesis history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Design, clone, and synthesis operations can spend Uydi credits. <br>
Mitigation: Check the credit balance and confirm user intent before paid operations; avoid blind retries and inspect history or voices after an uncertain failure. <br>
Risk: Voice cloning uploads an audio sample and can create a digital voice. <br>
Mitigation: Clone only voices the user owns or has explicit permission to use, and complete OAuth only on the expected Uydi site. <br>
Risk: Voice deletion is permanent when explicitly commanded. <br>
Mitigation: List voices first, verify the intended voice ID with the user, and delete only after explicit confirmation. <br>
Risk: OAuth credentials authorize access to the user's Uydi voices, credits, and synthesis history. <br>
Mitigation: Use logout or the Uydi website to revoke access when the skill is no longer needed. <br>


## Reference(s): <br>
- [Uydi homepage](https://uydi.com) <br>
- [ClawHub skill listing](https://clawhub.ai/lvyinchao/skills/uydi-voice) <br>
- [Official archive checksum](https://uydi.com/downloads/uydi-voice-skill.zip.sha256) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and local WAV file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, browser or device-code OAuth approval, and an optional UYDI_BASE_URL setting for development or self-hosted deployments.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
