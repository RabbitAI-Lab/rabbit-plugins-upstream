## Description: <br>
Voice Notes Pro transcribes WhatsApp voice notes with OpenAI Whisper and saves categorized Markdown notes for songs, tasks, shopping, ideas, people, and watchlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[toniaczlog](https://clawhub.ai/user/toniaczlog) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and automation builders use this skill to turn WhatsApp audio messages into local Markdown notes grouped by common personal productivity categories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WhatsApp voice audio is sent to OpenAI for transcription. <br>
Mitigation: Install only when users are comfortable with that data flow and have appropriate consent for any recorded personal information. <br>
Risk: Transcribed notes may include sensitive personal details stored in local Markdown files. <br>
Mitigation: Use a protected, user-owned notes directory and avoid storing sensitive details unless the user has decided they are appropriate to retain. <br>
Risk: The skill requires an OpenAI API key in the runtime environment. <br>
Mitigation: Protect OPENAI_API_KEY as a secret and do not commit or print it in logs or shared configuration. <br>
Risk: Default note paths point to /root/notes in the artifact configuration. <br>
Mitigation: Change the directories to an appropriate user-owned location before production use. <br>


## Reference(s): <br>
- [Voice Notes Pro ClawHub release page](https://clawhub.ai/toniaczlog/skills/voice-notes-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration guidance] <br>
**Output Format:** [Short text status messages and categorized Markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes notes to configured local directories and uses timestamps in saved Markdown entries.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
