## Description: <br>
小红书内容引擎 helps agents deconstruct Xiaohongshu posts and generate brand-aligned scripts, captions, image prompts, cover copy, tags, and optional media workflows from reference links and a shared content graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dizhu](https://clawhub.ai/user/dizhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content marketers, brand operators, and agents use this skill to analyze Xiaohongshu reference posts and turn the findings into structured deconstruction cards, brand-aware copy, image prompts, cover text, tags, and generation plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: XHS links, prompts, brand context, and generated media requests may be sent to configured crawler, LLM, image, and video providers. <br>
Mitigation: Use only providers authorized to process the content, keep provider keys in controlled environment files, and review generated reports before sharing them. <br>
Risk: Custom BASE_URL settings can route requests to untrusted endpoints. <br>
Mitigation: Keep AGENT_DELU_BASE_URL, OFOX_BASE_URL, OPENROUTER_BASE_URL, and ARK_BASE_URL under user control and avoid untrusted hosts. <br>
Risk: Seedance video generation can start paid jobs. <br>
Mitigation: Keep the default confirmation countdown or use prompt-only modes unless paid video generation is intentional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dizhu/skills/xhs-content-engine) <br>
- [Configuration guide](artifact/references/configuration.md) <br>
- [Output template](artifact/references/output-template.md) <br>
- [Example video output](artifact/references/example-video.md) <br>
- [Example image output](artifact/references/example-image.md) <br>
- [Ofox](https://ofox.ai) <br>
- [OpenRouter](https://openrouter.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown reports, generated copy, prompts, JSON workspace files, shell commands, and optional media asset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local deconstruction files, generated scripts, image or video prompts, media assets, and quality reports depending on the selected mode and configured providers.] <br>

## Skill Version(s): <br>
0.3.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
