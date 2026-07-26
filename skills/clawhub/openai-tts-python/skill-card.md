## Description: <br>
Converts text to natural-sounding speech using OpenAI's TTS API and writes audio files in mp3, opus, aac, or flac format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[merend](https://clawhub.ai/user/merend) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, employees, and external users use this skill to convert supplied text, files, or piped input into speech for accessibility, multitasking, narration, or podcast-style audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for conversion is processed by OpenAI and API usage may incur charges. <br>
Mitigation: Avoid secrets, regulated data, or confidential documents unless policy allows it, and review the text before sending it to the API. <br>
Risk: Broad activation terms such as voice, audio, or podcast could trigger the skill when text-to-speech output was not intended. <br>
Mitigation: Invoke the skill only for explicit TTS or audio-generation requests and confirm the requested content before execution. <br>
Risk: The script can read local text files and write generated audio files. <br>
Mitigation: Verify input file paths and output destinations before running commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/merend/skills/openai-tts-python) <br>
- [OpenAI TTS Documentation](https://platform.openai.com/docs/guides/text-to-speech) <br>
- [OpenAI Audio Speech API Reference](https://platform.openai.com/docs/api-reference/audio/createSpeech) <br>
- [OpenAI Pricing](https://openai.com/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with Python and bash examples; generated audio files in mp3, opus, aac, or flac format.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENAI_API_KEY; supports OpenAI TTS voices, tts-1 or tts-1-hd models, speed from 0.25x to 4.0x, and automatic chunking for text over 4096 characters.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
