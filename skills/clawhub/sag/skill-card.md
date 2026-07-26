## Description: <br>
ElevenLabs text-to-speech with mac-style say UX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Sag to turn text responses into ElevenLabs speech, preview voices, and generate local audio playback or audio files from command-line prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the required sag CLI from a Homebrew tap can execute third-party software outside the skill artifact. <br>
Mitigation: Verify that the Homebrew tap and sag CLI are trusted before installation. <br>
Risk: Using ElevenLabs text-to-speech sends submitted text to an external service and may consume paid API quota. <br>
Mitigation: Use a revocable ElevenLabs API key, monitor usage or billing, and avoid sending secrets or confidential text unless ElevenLabs processing is acceptable. <br>
Risk: Generated voice output may use the wrong speaker, delivery, or pronunciation for long responses. <br>
Mitigation: Confirm the voice and speaker before long output and use the documented normalization, language, and pause controls. <br>


## Reference(s): <br>
- [Sag homepage](https://sag.sh) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/sag) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>
- [Homebrew install formula](steipete/tap/sag) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance, files] <br>
**Output Format:** [Markdown with inline bash commands and optional MEDIA file references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local MP3 audio files through the sag CLI; requires ELEVENLABS_API_KEY and the sag binary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
