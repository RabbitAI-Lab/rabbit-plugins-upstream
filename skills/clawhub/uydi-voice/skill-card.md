## Description: <br>
Uydi Voice enables an AI agent to design custom voices, clone a user's authorized voice sample, and synthesize narration with the Uydi voice platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvyinchao](https://clawhub.ai/user/lvyinchao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Uydi voice workflows from an agent, including voice design, authorized voice cloning, text-to-speech, voice management, credit checks, and synthesis history review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice samples and generated speech are processed through the Uydi platform. <br>
Mitigation: Install and use the skill only when the user trusts Uydi with the uploaded samples and generated speech. <br>
Risk: Design, clone, and text-to-speech operations can consume real Uydi credits. <br>
Mitigation: Check credits before paid operations, confirm user intent before large synthesis work, and inspect history or voices before retrying uncertain paid requests. <br>
Risk: Voice cloning can be misused without consent. <br>
Mitigation: Clone only voices the user owns or has explicit permission to use. <br>
Risk: OAuth credentials are retained locally after login. <br>
Mitigation: Have the user complete OAuth themselves and run logout when they no longer want the local token retained. <br>


## Reference(s): <br>
- [Uydi homepage](https://uydi.com) <br>
- [Uydi Voice ClawHub listing](https://clawhub.ai/lvyinchao/skills/uydi-voice) <br>
- [Official archive checksum](https://uydi.com/downloads/uydi-voice-skill.zip.sha256) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, Files] <br>
**Output Format:** [Command-line text and WAV audio files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+, OAuth approval, and a Uydi account; design, clone, and text-to-speech operations can consume account credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
