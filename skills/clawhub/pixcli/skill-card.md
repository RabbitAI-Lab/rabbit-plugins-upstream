## Description: <br>
Pixcli helps agents generate and edit creative assets including images, video, voiceover, music, sound effects, podcasts, and Remotion-based video assemblies through the pixcli CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cohnen](https://clawhub.ai/user/cohnen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and agents use Pixcli to produce images, videos, audio, podcasts, and reusable Remotion video projects for product marketing, social media, explainers, and other content pipelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, audio samples, and generated media may be sent to the pixcli service and backend providers. <br>
Mitigation: Use the skill only for content approved for external processing, and avoid sensitive or regulated media unless the deployment has reviewed the service terms and data handling. <br>
Risk: Generated assets can be published through share links, and the evidence notes uncertainty around whether some shared links are permanent or expiring. <br>
Mitigation: Prefer private or unpublished outputs for sensitive work, set explicit TTLs when publishing, and review links before sharing them outside the intended audience. <br>
Risk: Voice cloning can create audio resembling a real speaker. <br>
Mitigation: Use voice cloning only with explicit authorization from the speaker and keep source samples and generated audio private unless publication is approved. <br>


## Reference(s): <br>
- [Pixcli homepage](https://pixcli.hilo.cx) <br>
- [Pixcli npm package](https://www.npmjs.com/package/pixcli) <br>
- [Command reference](references/command-reference.md) <br>
- [Creative guidelines](references/creative-guidelines.md) <br>
- [Prompt cookbook](references/prompt-cookbook.md) <br>
- [Remotion playbook](references/remotion-playbook.md) <br>
- [Template showcase](references/template-showcase.md) <br>
- [Workflow recipes](references/workflow-recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, shell commands, JSON CLI responses, generated media files, and Remotion project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media may include images, videos, audio files, podcasts, public or private share links, and Remotion renders.] <br>

## Skill Version(s): <br>
3.4.2 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
