## Description: <br>
Image Recognize uses Baidu AI to recognize objects, scenes, text, faces, plants, animals, products, and other categories in local, URL, or Base64 images and returns Markdown results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and general users use this skill to classify image content from local files, image URLs, or Base64 input with Baidu AI. It returns recognition details, confidence, category tags, and optional similar images in Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images, fetched image URLs, and visible text or faces in those images are sent to Baidu Qianfan for processing. <br>
Mitigation: Use only images appropriate for Baidu processing, and avoid private or internal URLs, sensitive photos, IDs, screenshots, medical images, and confidential documents. <br>
Risk: The Baidu API key is sensitive credential material. <br>
Mitigation: Set BAIDU_API_KEY in the environment instead of pasting it into chat, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/image-recognize) <br>
- [Baidu Qianfan](https://qianfan.baidubce.com) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, guidance] <br>
**Output Format:** [Markdown recognition report with optional shell command execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and BAIDU_API_KEY; image input may be a local path, URL, or Base64 string, with optional similar image count.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
