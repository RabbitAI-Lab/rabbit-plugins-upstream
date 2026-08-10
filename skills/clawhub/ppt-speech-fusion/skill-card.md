## Description: <br>
This skill helps users transcribe Chinese meeting recordings with Whisper and fuse optional PPT, image, or PDF materials into meeting minutes, transcript text, or page-aligned speech reconstruction PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulei223344-lang](https://clawhub.ai/user/fulei223344-lang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to turn authorized Chinese meeting recordings, with optional PPT, PDF, or image materials, into aligned speech reconstruction PDFs, Word meeting minutes, or plain transcript text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes meeting recordings and companion documents that may contain confidential, personal, or business-sensitive information. <br>
Mitigation: Use it only with recordings and materials the user is authorized to process, prefer an isolated workspace, and remove intermediate files when work is complete. <br>
Risk: The workflow can install unpinned Python packages and invoke local media or document tools. <br>
Mitigation: Review the commands before execution, run in a disposable virtual environment or container, and pin or audit dependencies before repeated use. <br>
Risk: Transcription and material alignment can be inaccurate when audio quality is poor or source materials do not match the recording. <br>
Mitigation: Review the generated transcript, meeting minutes, and PDF page alignment against the source recording and materials before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fulei223344-lang/skills/ppt-speech-fusion) <br>
- [Publisher profile](https://clawhub.ai/user/fulei223344-lang) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell and Python snippets; generated PDF, Word, or TXT files for end users.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install Python packages and invoke local media or document tools while processing user-supplied recordings and materials.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
