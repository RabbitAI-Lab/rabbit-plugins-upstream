## Description: <br>
DynaPictures helps agents list templates, retrieve template details, and generate hosted image URLs through an OOMOL-connected DynaPictures account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate DynaPictures through a connected OOMOL account, including listing API-ready templates, reading template layers, and generating hosted images from templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image generation can create hosted outputs and consume account credits. <br>
Mitigation: Require explicit user approval for generate_images, including the template, payload, expected credit use, and where hosted image URLs may be exposed. <br>
Risk: Template listing and retrieval may expose DynaPictures template metadata from the connected account. <br>
Mitigation: Treat list_templates and get_template as lower-risk read actions, but share returned template details only with the requesting user context. <br>


## Reference(s): <br>
- [DynaPictures homepage](https://dynapictures.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dynapictures) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted image URLs and connector execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
