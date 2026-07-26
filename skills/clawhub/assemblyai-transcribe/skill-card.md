## Description: <br>
Transcribe, diarize, translate, post-process, and structure audio or video with AssemblyAI for speaker-aware Markdown, normalized JSON, subtitles, and downstream agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to run AssemblyAI transcription workflows for local files or URLs, then export transcripts, speaker mappings, summaries, subtitles, and structured data for human review or downstream automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected media, transcript text, prompts, and configured URLs to AssemblyAI services. <br>
Mitigation: Use only approved media, treat recordings and transcripts as sensitive data, and configure EU endpoints when regional processing is required. <br>
Risk: The skill includes a transcript deletion command that can remove remote data without confirmation. <br>
Mitigation: Avoid exposing the delete command to automated workflows unless explicit user approval or separate safeguards are in place. <br>
Risk: The skill requires AssemblyAI API credentials. <br>
Mitigation: Provide ASSEMBLYAI_API_KEY through environment injection and keep API keys out of chat logs and generated artifacts. <br>


## Reference(s): <br>
- [AssemblyAI documentation](https://www.assemblyai.com/docs) <br>
- [AssemblyAI capabilities reference](references/capabilities.md) <br>
- [Workflow recipes](references/workflows.md) <br>
- [Output formats](references/output-formats.md) <br>
- [Speaker mapping reference](references/speaker-mapping.md) <br>
- [LLM Gateway notes](references/llm-gateway.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/assemblyai-transcribe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated transcript bundles can include Markdown, normalized JSON, raw JSON, text, SRT/VTT subtitles, and manifests.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and ASSEMBLYAI_API_KEY; supports configurable US or EU AssemblyAI endpoints.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
