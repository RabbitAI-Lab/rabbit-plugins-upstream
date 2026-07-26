## Description: <br>
Translates song lyrics between Chinese and other languages with attention to line alignment, singability, rhyme, cultural context, genre conventions, and bilingual output formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sakurakilove](https://clawhub.ai/user/sakurakilove) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to translate lyrics, create line-by-line bilingual renderings, add cultural notes, preserve musical phrasing, and format outputs for chat or files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may look up lyrics or reference translations when given only a song name or URL. <br>
Mitigation: Use sources the user is authorized to access, and ask for pasted lyrics or an explicit source preference when rights, privacy, or accuracy matter. <br>
Risk: Bundled examples include substantial copyrighted lyrics. <br>
Mitigation: Avoid redistributing bundled examples and review generated translations before publication or commercial reuse. <br>
Risk: The artifact documents fixed file-output examples under /home/z. <br>
Mitigation: Require an explicit save location before writing files and avoid relying on the documented fixed path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sakurakilove/skills/song-translation-expert) <br>
- [Translation principles](artifact/references/translation_principles.md) <br>
- [Special elements guide](artifact/references/special_elements.md) <br>
- [Output formats](artifact/references/output_formats.md) <br>
- [Quality checklist](artifact/references/quality_checklist.md) <br>
- [English songs guide](artifact/references/english_songs.md) <br>
- [Japanese songs guide](artifact/references/japanese_songs.md) <br>
- [World songs guide](artifact/references/world_songs.md) <br>
- [Sample corpus README](artifact/assets/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown line-by-line lyric translations by default, with optional tables, JSON, LRC-style text, or file-generation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source lyrics, translated lines, metadata, section markers, cultural notes, and quality-check results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
