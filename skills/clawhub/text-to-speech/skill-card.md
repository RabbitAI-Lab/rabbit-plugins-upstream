## Description: <br>
Convert text to natural speech with DIA TTS, Kokoro, Chatterbox, and more via inference.sh CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and teams use this skill to generate natural speech, voiceovers, audiobook narration, podcasts, accessibility audio, IVR prompts, and video narration through inference.sh audio apps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a remote CLI installer and hosted inference.sh processing. <br>
Mitigation: Install only when inference.sh and the infsh CLI are trusted; use the checksum-verified manual install path when stronger supply-chain assurance is required. <br>
Risk: Text, scripts, private URLs, personal data, regulated content, or cloned voices may be sent to hosted processing. <br>
Mitigation: Avoid submitting confidential or regulated inputs, and only use cloned voices with consent and an acceptable data-handling arrangement. <br>


## Reference(s): <br>
- [Text To Speech skill page](https://clawhub.ai/okaris/skills/text-to-speech) <br>
- [Publisher profile](https://clawhub.ai/user/okaris) <br>
- [inference.sh](https://inference.sh) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [Apps Overview](https://inference.sh/docs/apps/overview) <br>
- [Manual install checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for invoking hosted inference.sh text-to-speech apps with user-provided text and optional voice or style settings.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
