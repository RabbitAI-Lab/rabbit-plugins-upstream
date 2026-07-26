## Description: <br>
Batch-generate images with the OpenAI Images API and create a local thumbnail gallery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative users can use this skill to generate batches of images from either sampled structured prompts or user-provided prompts, then review the generated PNG files through a local HTML gallery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an OpenAI API key and sends image prompts to OpenAI. <br>
Mitigation: Use an approved API key handling process and avoid including secrets, private personal data, or confidential business material in prompts unless approved for the environment. <br>
Risk: Generated images and prompt mappings are written to the configured local output directory. <br>
Mitigation: Choose an appropriate output directory and review generated files before sharing or retaining them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/openai-image-gen) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated runtime artifacts include PNG images, prompts.json, and an index.html gallery.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENAI_API_KEY or an explicit API key argument; supports count, model, size, quality, prompt, timeout, sleep, output directory, and dry-run options.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
