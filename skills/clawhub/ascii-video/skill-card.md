## Description: <br>
Convert video to ASCII animation with multiple dithering modes, color output, and framerate control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative coders, terminal artists, and documentation authors use this skill to convert video or image inputs into ASCII previews or animations with width, frame-rate, charset, and color controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI invokes ffmpeg and processes local media files, so malformed or untrusted media could expose the local media toolchain to parser vulnerabilities. <br>
Mitigation: Run conversions in a sandbox or disposable workspace, keep ffmpeg and Pillow patched, and process only files the user intended to convert. <br>
Risk: The bundled CI verifier can execute Python files and self-test commands in target folders. <br>
Mitigation: Run the verifier only on trusted skill folders or inside a sandbox. <br>
Risk: The quick-start path downloads a raw Python script before execution. <br>
Mitigation: Review, pin, or checksum the script source before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/ascii-video) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated ASCII text, GIF, or MP4 files from the CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-selected media input, width, frame rate, charset, color mode, and target file path.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence; artifact frontmatter lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
