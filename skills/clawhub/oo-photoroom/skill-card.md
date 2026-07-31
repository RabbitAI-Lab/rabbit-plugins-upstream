## Description: <br>
Photoroom helps agents operate Photoroom through an OOMOL-connected account, including controlled ecommerce product-image edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to edit product images in Photoroom from an image URL and retrieve an edited result URL. It is suited for ecommerce image workflows where write actions are reviewed before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke a write-tagged Photoroom image-editing operation. <br>
Mitigation: Confirm the exact payload and expected image-editing effect with the user before running the action. <br>
Risk: Edited images may use relighting, text removal, or beautification that changes product presentation. <br>
Mitigation: Have a human review edited images before publishing them in ecommerce workflows. <br>
Risk: The workflow may use OOMOL transit storage for generated image results. <br>
Mitigation: Use the skill only with an intended OOMOL-connected Photoroom account and avoid submitting sensitive image URLs unless that storage path is acceptable. <br>


## Reference(s): <br>
- [Photoroom homepage](https://www.photoroom.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-photoroom) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Photoroom connector JSON containing a resultUrl and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
