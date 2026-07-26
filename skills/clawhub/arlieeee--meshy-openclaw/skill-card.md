## Description: <br>
Generate 3D models, textures, images, rigged characters, animations, and 3D-print-ready assets through the Meshy AI API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Arlieeee](https://clawhub.ai/user/Arlieeee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, makers, and agent users can use this skill to create or transform Meshy assets from prompts or images, then download models and prepare OBJ files for slicers when 3D printing is requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meshy API requests send the user's generation prompts, image URLs, and selected local images to Meshy. <br>
Mitigation: Use the skill only for content that is appropriate to share with Meshy, and avoid submitting confidential prompts or images unless that data sharing is acceptable. <br>
Risk: The skill requires MESHY_API_KEY and can spend Meshy API credits when generation, refinement, rigging, animation, or image tasks are confirmed. <br>
Mitigation: Keep MESHY_API_KEY in a project-specific environment or .env file outside version control, and review the cost confirmation before approving API tasks. <br>
Risk: Generated Meshy assets may need prompt, geometry, scale, orientation, or slicer review before practical use or 3D printing. <br>
Mitigation: Inspect downloaded model files and slicer previews before relying on the output, especially for physical prints or downstream production work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Arlieeee/meshy-openclaw) <br>
- [Meshy API documentation](https://docs.meshy.ai) <br>
- [Meshy API endpoint](https://api.meshy.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash and Python code blocks plus downloaded 3D asset files and metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MESHY_API_KEY, python3, curl, and the Python requests package; generated assets are organized under meshy_output/.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
