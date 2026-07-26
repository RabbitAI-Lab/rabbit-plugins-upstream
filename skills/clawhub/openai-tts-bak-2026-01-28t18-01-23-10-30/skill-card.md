## Description: <br>
Text-to-speech via OpenAI Audio Speech API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nicoataiza](https://clawhub.ai/user/nicoataiza) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to generate speech audio from text through OpenAI's Audio Speech API, with configurable voice, model, format, speed, and output path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text passed to the skill is sent to OpenAI for speech generation. <br>
Mitigation: Do not submit secrets, regulated data, or private content unless policy allows that external processing. <br>
Risk: The skill uses the configured OpenAI API key and may incur API charges. <br>
Mitigation: Use an approved API key, protect stored credentials, and monitor usage before running large text workloads. <br>
Risk: The shell script depends on jq even though the metadata only lists curl. <br>
Mitigation: Install jq before use and verify the local environment has both curl and jq available. <br>


## Reference(s): <br>
- [OpenAI Text-to-Speech Guide](https://platform.openai.com/docs/guides/text-to-speech) <br>
- [ClawHub Skill Page](https://clawhub.ai/nicoataiza/skills/openai-tts-bak-2026-01-28t18-01-23-10-30) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Audio files, Configuration guidance] <br>
**Output Format:** [Shell command output and generated audio in mp3, opus, aac, flac, wav, or pcm format] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and OPENAI_API_KEY; can stream audio to stdout or write it to a file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
