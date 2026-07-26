## Description: <br>
Generate professional product photography and commercial image prompts using inference.sh models such as FLUX, Imagen 3, Grok, and Seedream. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Marketing teams, e-commerce operators, designers, and developers use this skill to create product-shot prompts, model-selection guidance, and inference.sh commands for listings, mockups, ads, and lifestyle product imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends product prompts or images to inference.sh as a hosted image-processing provider. <br>
Mitigation: Use only product imagery and data your organization permits for hosted processing, and avoid unreleased or regulated product material unless approved. <br>
Risk: The quick start uses a curl-piped shell installer for the inference.sh CLI. <br>
Mitigation: Review the installer before running it or use the documented checksum verification path for manual installation. <br>
Risk: The skill requires inference.sh login credentials for CLI use. <br>
Mitigation: Treat infsh login credentials like service tokens and rotate or revoke them according to organizational policy. <br>


## Reference(s): <br>
- [Ai Product Photography on ClawHub](https://clawhub.ai/okaris/skills/ai-product-photography) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI installer](https://cli.inference.sh) <br>
- [inference.sh CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the inference.sh CLI and may produce JSON response files that reference generated image outputs.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
