## Description:

Writes and converts text into natural speech-ready output for any TTS engine: normalization, prosody, pronunciation, and voice preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent builders use this skill to turn written replies, briefings, notifications, and dialogue turns into text that is ready for speech synthesis. It helps agents normalize tokens, manage pronunciation and voice preferences, adapt to listening contexts, and fall back cleanly when a TTS engine cannot produce suitable audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent speech preferences may record voice choices, locale, pronunciation fixes, quiet hours, and engine notes.

Mitigation: Keep preference memory scoped to ~/Clawic/data/speak/ and review stored config or preference files before sharing or deploying the skill.

Risk: Cloud TTS providers may receive spoken text that leaves the local machine.

Mitigation: Review the selected TTS provider separately and use local or approved engines for sensitive, regulated, or private content.

Risk: Sensitive content can be exposed if read aloud in a shared or public space.

Mitigation: Use the skill's shared-space and notification rules: speak only high-level alerts and keep codes, balances, medical content, and third-party message bodies in text unless the user explicitly asks for them aloud.

Risk: Unsupported SSML can be read aloud as literal tags or cause synthesis failure.

Mitigation: Test one tag per engine, store the supported tier in preferences, and fall back to punctuation-only speech when SSML support is absent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/speak)
- [Clawic Skill Page](https://clawic.com/skills/speak)
- [Setup](artifact/setup.md)
- [Engines](artifact/engines.md)
- [SSML](artifact/ssml.md)
- [Audiences And Contexts](artifact/audiences.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Plain text or Markdown guidance with optional YAML and preference-memory snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces speech-ready text and scoped preference updates for voice, rate, locale, pronunciation, listening context, and engine behavior.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
