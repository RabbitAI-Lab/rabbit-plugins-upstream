## Description: <br>
Create AI marketing videos for ads, promos, product launches, and brand content using inference.sh CLI workflows for visual generation, voiceover, and media assembly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Marketing teams, creators, and developers use this skill to generate platform-specific promotional videos, product demos, testimonials, explainers, social ads, and voiceover-supported campaign variants through inference.sh commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick start pipes a remote CLI installer into a shell. <br>
Mitigation: Review the installer before execution or use manual download with checksum verification from the published checksum file. <br>
Risk: The workflows send prompts and campaign materials to external AI services through inference.sh. <br>
Mitigation: Do not submit secrets, unreleased campaign details, customer data, or regulated personal data unless organizational policy allows that processing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/ai-marketing-videos) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI checksum file](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command templates and JSON CLI inputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call external inference.sh apps and may produce JSON files, generated video assets, audio, and merged media outputs outside the skill itself.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
