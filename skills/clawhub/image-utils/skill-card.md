## Description: <br>
Classic image manipulation with Python Pillow for resizing, cropping, compositing, format conversion, watermarks, brightness and contrast adjustments, and web optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galbria](https://clawhub.ai/user/galbria) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content production teams use this skill to post-process existing images, prepare web and social media variants, batch process image directories, and convert or optimize image formats with deterministic Pillow operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Loading images from arbitrary URLs can expose private or internal URLs and can fetch untrusted image content. <br>
Mitigation: Use trusted public image URLs, avoid private/internal sources, and review downloaded images before relying on processed outputs. <br>
Risk: The Bria integration example sends prompts and image retrieval through a third-party API. <br>
Mitigation: Send only prompts and images intended for the remote service, and configure BRIA_API_KEY only in environments approved for that API use. <br>
Risk: Batch processing and save operations write processed image files locally. <br>
Mitigation: Choose output directories deliberately, avoid sensitive source images unless local writes are acceptable, and review generated files before deployment. <br>


## Reference(s): <br>
- [image_utils.py API reference](references/code-examples/image_utils.py) <br>
- [bria-ai skill](https://clawhub.ai/galbria/bria-ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, files] <br>
**Output Format:** [Markdown with Python and shell code blocks; Python utilities produce image files, image bytes, or base64 strings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Pillow and requests for the documented examples; optional Bria API integration uses BRIA_API_KEY.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
