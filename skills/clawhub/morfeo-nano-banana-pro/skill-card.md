## Description: <br>
Generates and edits images with Google's Nano Banana Pro (Gemini 3 Pro Image) API, including text-to-image generation, image-to-image editing, reference-image guidance, and selectable 1K, 2K, or 4K resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to generate new images, edit existing images, or create product, style, character, and subject-consistent visual assets through Google's image generation API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected input or reference images are sent to Google for processing. <br>
Mitigation: Use only content that is appropriate to upload to Google, and avoid sensitive personal, confidential, or regulated images unless that transfer is acceptable. <br>
Risk: Generated or edited images are written to local output paths and could overwrite existing files. <br>
Mitigation: Choose output filenames carefully and review destination paths before running the generation command. <br>
Risk: Passing an API key directly on the command line can expose it through shell history or process listings. <br>
Mitigation: Prefer the GEMINI_API_KEY environment variable for API key configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pauldelavallaz/skills/morfeo-nano-banana-pro) <br>
- [Google AI Studio generateContent endpoint](https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=${API_KEY}) <br>
- [Vertex AI Gemini image prediction endpoint](https://${REGION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/publishers/google/models/gemini-3-pro-image-preview:predict) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and locally saved image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports prompts, optional input images, optional reference images, reference type selection, aspect ratio, resolution, number of images, and API key configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
