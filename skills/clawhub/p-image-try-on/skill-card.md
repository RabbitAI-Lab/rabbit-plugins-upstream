## Description: <br>
Use when someone wants virtual try-on: dress a person in clothes from reference photos for fashion or ecommerce. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare Pruna virtual try-on requests from a person image, garment reference images, and optional pose or disambiguation inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected person, garment, and optional pose images are sent to Pruna's external service using PRUNA_API_KEY. <br>
Mitigation: Use only approved images, avoid sensitive photos unless needed, and confirm cost and inputs before generation. <br>
Risk: Ambiguous garment references can produce incorrect try-on outputs or unintended changes to the person, pose, or garments. <br>
Mitigation: Confirm person_image and garment_images before API calls and show the optional disambiguation prompt when references are ambiguous. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on) <br>
- [Pruna file upload API](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-selected image URLs; may produce Pruna API request guidance and generation commands.] <br>

## Skill Version(s): <br>
1.0.7 (source: server evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
