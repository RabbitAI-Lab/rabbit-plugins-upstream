## Description:

Search and retrieve Quranic verses, surahs, pages, or juz with Arabic text and metadata using the alquran.cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[m7madash](https://clawhub.ai/user/m7madash)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Quranic content by surah, ayah, page, or juz and return Arabic verse text with related metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quran lookup requests are sent to the external api.alquran.cloud service.

Mitigation: Use the skill only when sending lookup parameters to that third-party API is acceptable.

Risk: The artifact currently provides Arabic-focused instructions and output.

Mitigation: Confirm that Arabic text and metadata meet the user's language and edition expectations before relying on the result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/m7madash/skills/quran-api)
- [alquran.cloud API](https://api.alquran.cloud/v1/)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown guidance with bash command examples and plain-text lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Arabic Quran text with surah, ayah, page, juz, revelation type, and related metadata when the external API is reachable.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
