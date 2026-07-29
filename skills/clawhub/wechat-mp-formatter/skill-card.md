## Description: <br>
公众号排版器 converts article content into self-contained, inline-styled HTML that can be copied into the WeChat Official Account editor while preserving supported formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pkutitan](https://clawhub.ai/user/pkutitan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to turn article titles, body copy, lyrics, quotes, highlights, and music metadata into WeChat-compatible HTML for publication workflows. It is especially suited to music, nostalgia, emotional, and lifestyle articles, with palette or component adjustments recommended for other topics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML may contain user-provided or untrusted article content that is opened locally and later copied into a publishing workflow. <br>
Mitigation: Review the generated HTML file and article content before opening, copying, or publishing it. <br>
Risk: Unsupported WeChat editor CSS can be stripped during paste, causing backgrounds, layout, or copy behavior to fail. <br>
Mitigation: Use the bundled compatibility rules: prefer section and table elements with inline styles, avoid flex, gradients, box-shadow, positioning, animation, and ClipboardItem. <br>


## Reference(s): <br>
- [WeChat Official Account CSS compatibility reference](references/compatibility.md) <br>
- [ClawHub skill page](https://clawhub.ai/pkutitan/skills/wechat-mp-formatter) <br>
- [Publisher profile](https://clawhub.ai/user/pkutitan) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Files, Guidance] <br>
**Output Format:** [Self-contained HTML file with inline CSS plus concise usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated article HTML is intended for local browser review, copy, and paste into the WeChat Official Account editor.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
