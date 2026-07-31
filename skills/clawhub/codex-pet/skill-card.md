## Description: <br>
Codex Pet — Pro Pack on RunComfy helps agents create a Codex-compatible custom pet from one reference image, producing a `pet.json` manifest and `spritesheet.webp` atlas for local Codex installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Codex users use this skill to turn a public source image into a local custom Codex Pet using RunComfy and ImageMagick, then install the generated files under their Codex pets directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The chosen public source image URL is sent through the RunComfy CLI to RunComfy/OpenAI. <br>
Mitigation: Use only image URLs that are acceptable to share with those services. <br>
Risk: The workflow writes generated pet files under the local Codex home directory. <br>
Mitigation: Review generated commands before execution, especially `PET_NAME`, `SOURCE_URL`, and the destination path. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/permew/skills/codex-pet) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI Documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=codex-pet) <br>
- [RunComfy GPT Image 2 Edit Endpoint](https://www.runcomfy.com/models/openai/gpt-image-2/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=codex-pet) <br>
- [RunComfy CLI Troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=codex-pet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and JSON manifest examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides generation of local Codex Pet files, typically `pet.json` and `spritesheet.webp`.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
