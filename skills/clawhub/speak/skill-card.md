## Description: <br>
Speak prepares written agent output for natural text-to-speech delivery by normalizing content, shaping prosody, managing pronunciation, and applying voice preferences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and voice-enabled agent users use Speak to rewrite replies, briefings, notifications, and dialogue turns into speech-ready text for TTS engines. It is also used to maintain voice, rate, locale, SSML, pronunciation, and listening-context preferences for future spoken interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can keep local speech preferences such as pronunciation fixes, locale, voice, rate, and context notes in ~/Clawic/data/speak/. <br>
Mitigation: Review or delete the local preference files when long-term personalization is not desired, especially for names, language preferences, and listening contexts. <br>
Risk: Spoken output can disclose sensitive information when other people can hear the audio. <br>
Mitigation: Keep codes, balances, medical details, and third-party message bodies in text unless the user explicitly asks for them aloud in a private context. <br>
Risk: Cloud TTS engines may receive the text prepared for speech. <br>
Mitigation: Use a local TTS engine or review the chosen provider's privacy and compliance terms before sending sensitive content to cloud synthesis. <br>


## Reference(s): <br>
- [Speak on ClawHub](https://clawhub.ai/ivangdavila/skills/speak) <br>
- [Speak homepage](https://clawic.com/skills/speak) <br>
- [Setup](setup.md) <br>
- [Memory Template](memory-template.md) <br>
- [Normalization](normalization.md) <br>
- [Pronunciation](pronunciation.md) <br>
- [SSML](ssml.md) <br>
- [Engines](engines.md) <br>
- [Audiences And Contexts](audiences.md) <br>
- [Notifications](notifications.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Speech-ready text and Markdown guidance with optional configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local speech preferences under ~/Clawic/data/speak/ when the user provides confirmed voice, rate, pronunciation, locale, or context preferences.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
