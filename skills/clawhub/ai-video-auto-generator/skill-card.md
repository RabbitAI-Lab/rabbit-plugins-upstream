## Description: <br>
AI video auto generator is an AI video pipeline that turns an idea or source document into a structured script, repaired prompts, generated assets, video, audio, subtitles, and a final video output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinxuchen2020](https://clawhub.ai/user/jinxuchen2020) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video creators use this skill to turn prompts, documents, URLs, or prepared script JSON into short-form AI video projects. The agent can generate and repair scripts, create project assets, run the video pipeline, and report completion status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The pipeline can install packages, run commands, and start background jobs. <br>
Mitigation: Review configuration before setup or auto mode, run in a controlled workspace, and avoid detached/background mode unless the process can be monitored and stopped. <br>
Risk: The skill can use global credentials and send assets or metadata to external services. <br>
Mitigation: Use dedicated low-scope tokens, prefer explicit local tracking with --tracker local, and avoid processing sensitive inputs unless third-party sharing is acceptable. <br>
Risk: Server security evidence reports scoping and documentation mismatches. <br>
Mitigation: Review the current release documentation and configuration paths before deployment, especially provider setup, credential handling, and generated output locations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinxuchen2020/skills/ai-video-auto-generator) <br>
- [README](README.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Provider configuration](references/provider-config.md) <br>
- [Script JSON checklist](references/script-json-checklist.md) <br>
- [Asset generation](references/asset-generation.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Agnes AI platform](https://platform.agnes-ai.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Files, Media files] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON script files, project files, generated assets, subtitles, and video outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install dependencies, start background jobs, and use third-party services for image, video, audio, and document workflows.] <br>

## Skill Version(s): <br>
2.7.1 (source: server release metadata; artifact frontmatter and changelog show 2.7.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
