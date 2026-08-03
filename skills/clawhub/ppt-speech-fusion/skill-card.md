## Description: <br>
Helps an agent transcribe Chinese meeting audio with Whisper and, when PPTX slides are provided, align the transcript with slide content to produce a speech-restoration PDF or meeting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulei223344-lang](https://clawhub.ai/user/fulei223344-lang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to turn meeting recordings, with optional PPTX slides, into Chinese transcripts, meeting minutes, or slide-aligned speech drafts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive meeting recordings and PPT files may include confidential or regulated content. <br>
Mitigation: Review the skill before installation, use a dedicated or virtual environment, and avoid processing sensitive recordings or slides unless storage and processing locations are understood. <br>
Risk: The skill can install unpinned packages at runtime. <br>
Mitigation: Approve dependencies explicitly and pin or preinstall reviewed package versions before running the workflow in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fulei223344-lang/skills/ppt-speech-fusion) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, code, shell commands, configuration, guidance] <br>
**Output Format:** [Transcript text, meeting-summary Markdown or Word content, and generated PDF/Word/txt files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dependency-check commands and local file paths for generated outputs.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
