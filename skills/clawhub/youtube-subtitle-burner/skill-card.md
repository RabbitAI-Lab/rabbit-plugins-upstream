## Description: <br>
Downloads YouTube videos, extracts word-level subtitle timing, translates subtitles to Chinese, and burns them into local H.264 MP4 files with PIL-based antialiased rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terryso](https://clawhub.ai/user/terryso) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media workflow operators use this skill to prepare Chinese-subtitled local MP4 versions of YouTube videos. It guides an agent through video download, json3 subtitle extraction, translation batching, preview generation, and final subtitle burn-in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may run an optional curl-based uv installer and a local Clash proxy command. <br>
Mitigation: Review those commands and run them only when the installer source, local proxy endpoint, and selected network route are trusted. <br>
Risk: The workflow downloads YouTube content and reads local media and subtitle files selected by the user. <br>
Mitigation: Use only content the user is allowed to process and keep input files in a controlled local workspace. <br>
Risk: The burn-in script writes to the output path supplied by the user. <br>
Mitigation: Choose a dedicated output filename, generate a short preview first, and avoid pointing output at an existing file that should be preserved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terryso/skills/youtube-subtitle-burner) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Subtitle burn-in script](artifact/scripts/burn_subtitles.py) <br>
- [json3 subtitle parser](artifact/scripts/parse_json3_subs.py) <br>
- [Subtitle translation helper](artifact/scripts/translate_subs.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown guidance with bash commands plus JSON subtitle files and MP4 video outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces parsed subtitle JSON, translated subtitle JSON templates, optional preview MP4 files, and burned H.264 MP4 files.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
