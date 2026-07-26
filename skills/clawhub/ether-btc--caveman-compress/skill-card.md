## Description: <br>
Compress workspace bootstrap files into caveman-speak to reduce input tokens on every session load, creating .original.md backups before overwriting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ether-btc](https://clawhub.ai/user/ether-btc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to shorten selected markdown workspace context files while preserving technical references and creating backups before rewrite. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local workspace file contents may be sent to Claude, MiniMax/OpenAI-compatible endpoints, or DeepSeek using credentials available in the environment. <br>
Mitigation: Use only explicit file paths intended for compression, avoid files containing secrets, and choose provider credentials deliberately. <br>
Risk: Rewritten workspace context files may lose or alter important operational detail if model compression is incorrect. <br>
Mitigation: Prefer dry-run and manual review before writing, and verify the .original.md backup before relying on compressed output. <br>
Risk: Security evidence says the skill's safety boundaries are weaker than the description suggests. <br>
Mitigation: Review the target file, provider path, and generated compressed text before deployment or repeated use. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ether-btc/caveman-compress) <br>
- [Upstream caveman project](https://github.com/JuliusBrussee/caveman) <br>
- [Brevity Constraints Reverse Performance Hierarchies](https://arxiv.org/abs/2604.00025) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown file content and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes compressed markdown in place when not run as dry-run and creates a .original.md backup before overwrite.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
