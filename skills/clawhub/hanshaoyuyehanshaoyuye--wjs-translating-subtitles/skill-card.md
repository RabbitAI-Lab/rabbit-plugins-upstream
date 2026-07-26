## Description: <br>
Translates SRT subtitle files or transcript text into target-language or bilingual SRT output, with punctuation-bounded re-segmentation so cues end at natural sentence breaks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hanshaoyuyehanshaoyuye](https://clawhub.ai/user/hanshaoyuyehanshaoyuye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, video editors, and localization workflows use this skill to translate existing SRT files or transcript text into readable target-language or bilingual subtitles while preserving timing and re-segmenting cues at natural punctuation boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the Python helper directly depends on a project-provided integration/translate_srt.py implementation. <br>
Mitigation: Confirm the intended integration module exists in the project before invoking artifact/scripts/translate.py. <br>
Risk: Chinese subtitle output defaults to Simplified Chinese and may not match projects that require Traditional Chinese. <br>
Mitigation: Specify Traditional Chinese explicitly when that script is required. <br>
Risk: Subtitle translation or re-segmentation can alter meaning, timing, or cue boundaries. <br>
Mitigation: Review generated SRT output for natural translation, valid timestamps, non-overlap, accurate proper nouns, and punctuation-bounded cues before handoff. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [SRT subtitle text, transcript text, or Markdown table] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce target-only SRT, bilingual SRT, target transcript, or side-by-side source/target table.] <br>

## Skill Version(s): <br>
8.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
