## Description: <br>
Guides agents through AI voice generation, text-to-speech, and voice synthesis workflows using the inference.sh CLI and supported voice models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and content teams use this skill to create voiceovers, audiobook or podcast narration, accessibility audio, and video voiceover workflows with inference.sh models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided text, media URLs, voice samples, portraits, and generated-content prompts may be sent to inference.sh. <br>
Mitigation: Do not submit secrets, regulated data, non-public media URLs, personal voice samples, portraits, or copyrighted content unless you have permission and accept the provider's data handling terms. <br>
Risk: The quick-start path uses a remote CLI installer and login flow. <br>
Mitigation: Install only if you trust inference.sh; prefer the manual checksum-verified install path when supply-chain risk matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/ai-voice-cloning) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI installer](https://cli.inference.sh) <br>
- [inference.sh CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON CLI payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference generated audio or media URLs returned by inference.sh.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
