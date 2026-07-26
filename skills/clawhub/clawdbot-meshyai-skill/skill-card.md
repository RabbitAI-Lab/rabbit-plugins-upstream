## Description: <br>
Use the Meshy.ai REST API to generate assets: (1) text-to-2d (Meshy Text to Image) and (2) image-to-3d, then download outputs locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sabatesduran](https://clawhub.ai/user/sabatesduran) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to call Meshy.ai from an agent workflow, create text-to-image or image-to-3D tasks, poll for completion, and save generated image or OBJ outputs locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected images are sent to Meshy.ai using the user's Meshy API key. <br>
Mitigation: Use only prompts and images that are appropriate to share with Meshy.ai, and keep MESHY_API_KEY scoped and protected. <br>
Risk: A custom MESHY_BASE_URL can redirect API calls away from the default Meshy endpoint. <br>
Mitigation: Use the default endpoint unless the custom endpoint is deliberately trusted. <br>
Risk: Generated assets are written to the configured local output directory. <br>
Mitigation: Choose an output directory where generated PNG, OBJ, and MTL files may be safely stored. <br>


## Reference(s): <br>
- [Meshy API Notes](references/api-notes.md) <br>
- [Meshy API Documentation](https://docs.meshy.ai/en) <br>
- [Meshy Text-to-Image API](https://docs.meshy.ai/en/api/text-to-image) <br>
- [Meshy Image-to-3D API](https://docs.meshy.ai/en/api/image-to-3d) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files may include PNG images, OBJ models, and optional MTL files saved under the configured output directory.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
