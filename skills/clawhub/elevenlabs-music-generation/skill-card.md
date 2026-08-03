## Description: <br>
Generate full songs and instrumental tracks with ElevenLabs Music on RunComfy through the `runcomfy` CLI, using structured prompts for vocals, instrumentals, jingles, theme music, and background tracks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide agents in creating music generation prompts and RunComfy CLI calls for songs, instrumental beds, jingles, podcast intros, game loops, and similar audio tracks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunComfy music generation may incur duration-based charges. <br>
Mitigation: Review pricing and confirm `music_length_ms` before generation; draft short tracks before longer final renders. <br>
Risk: RunComfy tokens can be exposed if copied into prompts, logs, or committed files. <br>
Mitigation: Use `RUNCOMFY_TOKEN` or the RunComfy config file, and avoid echoing or storing tokens in generated content. <br>
Risk: Generated songs based on user-supplied lyrics may raise rights or licensing issues. <br>
Mitigation: Confirm the user has rights to supplied lyrics before generating music around them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/elevenlabs-music-generation) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [ElevenLabs Music model page](https://www.runcomfy.com/models/elevenlabs/elevenlabs/music-generation?utm_source=clawhub&utm_medium=skill&utm_campaign=elevenlabs-music-generation) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=elevenlabs-music-generation) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=elevenlabs-music-generation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides a RunComfy CLI call that downloads generated audio into the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
