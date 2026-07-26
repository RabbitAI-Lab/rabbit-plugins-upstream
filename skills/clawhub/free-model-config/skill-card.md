## Description: <br>
Free Model Config helps agents standardize free AI model setup across Agnes AI, Zhipu, SenseNova, Xiaomi MIMO, and Meituan LongCat, including API-key guidance, model selection, configuration generation, and optional multimodal media workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and advanced users use this skill to select free AI model providers, generate API and model configuration guidance, and optionally run helper scripts for Agnes AI multimodal media generation, TTS audio, and media merging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read model API keys from command-line arguments, environment variables, or local configuration and send prompts or generated content to external services. <br>
Mitigation: Use placeholders in shared material, keep real keys in environment variables or a secret manager, and review generated commands before execution. <br>
Risk: The multimodal workflow can upload local images to public third-party hosts before video generation. <br>
Mitigation: Use only public or non-sensitive images, or replace the upload path with approved private storage before running that workflow. <br>
Risk: Security evidence reports a suspicious verdict and unsafe instruction-scoping language. <br>
Mitigation: Treat artifact instructions as untrusted task content, review behavior before installation, and run security scanning before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/free-model-config) <br>
- [Free Model Config catalog](references/fmc-catalog.md) <br>
- [Free Model Config requirements](references/fmc-requirements.md) <br>
- [Free Model Config exemplars](references/exemplars.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell command examples, and optional generated media files when helper scripts are executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference MODEL_API_KEY, ~/.workbuddy/models.json, ffmpeg, edge-tts, and platform-specific API endpoints depending on the selected workflow.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
