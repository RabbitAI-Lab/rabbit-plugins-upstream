## Description: <br>
Speech-To-Text with MLX (Apple Silicon) and opensource models (default GLM-ASR-Nano-2512) locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoqiao](https://clawhub.ai/user/guoqiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill on Apple Silicon Macs to transcribe local audio files into text with MLX and open-source speech-to-text models, without using an external API or server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation may add or update local audio and ML tooling through Homebrew and uv. <br>
Mitigation: Review the install script and run it only in an environment where Homebrew and uv package changes are acceptable. <br>
Risk: Audio transcripts are printed into the agent session and may expose sensitive spoken content. <br>
Mitigation: Use explicit invocation with /mlx-stt <audio> and avoid transcribing sensitive audio in shared or logged sessions. <br>
Risk: The skill is intended for macOS on Apple Silicon and may not work on other platforms. <br>
Mitigation: Deploy it only on Darwin hosts with Apple Silicon and the required brew dependency available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guoqiao/skills/mlx-stt) <br>
- [Metadata homepage](https://github.com/guoqiao/skills/blob/main/mlx-stt/mlx-stt/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text transcript with Markdown usage guidance and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Transcript text is printed to stdout and may appear in the agent session.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
