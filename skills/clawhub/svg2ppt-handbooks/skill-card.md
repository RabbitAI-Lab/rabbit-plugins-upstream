## Description: <br>
Convert SVG content, Chinese character stroke order, province/country maps (Chinese, English or pinyin names like Anhui/China/USA/Japan), or SVG URLs into editable PowerPoint (.pptx) via the handbooks.cn SVG-to-PPT service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glandon](https://clawhub.ai/user/glandon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert SVG content, SVG URLs, Chinese character stroke-order requests, and map requests into editable PowerPoint files through the Handbooks SVG-to-PPT service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversion inputs, SVG URLs, map or character requests, and the user's Handbooks API key are sent to handbooks.cn. <br>
Mitigation: Use the skill only when that external service is acceptable for the data; avoid confidential diagrams, internal URLs, and proprietary SVGs. <br>
Risk: The bundled command-line script accepts the API key as an argument or via manual invocation. <br>
Mitigation: Provide a key only when actively converting content, and prefer workflows that avoid persisting keys in reusable scripts or shared logs. <br>


## Reference(s): <br>
- [Handbooks SVG to PPT Tool](https://www.handbooks.cn/svg2ppt.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/glandon/skills/svg2ppt-handbooks) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, JSON] <br>
**Output Format:** [Markdown guidance and JSON API responses with PowerPoint download links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful conversions return a download URL, file name, and link expiration; the skill documentation says download links are valid for about 7 days.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
