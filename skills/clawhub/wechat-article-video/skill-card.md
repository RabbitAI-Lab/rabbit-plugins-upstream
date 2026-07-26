## Description: <br>
Convert Chinese WeChat public-account articles and supplied images into publish-ready vertical WeChat Channels videos, including article analysis, fact-safe scripting, 9:16 layout direction, Edge TTS narration, subtitle synchronization, HyperFrames or Remotion rendering, visible first-frame covers, and delivery QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, video production operators, and WeChat content teams use this skill to turn Chinese public-account articles and supplied images into complete vertical WeChat Channels video packages. It is especially suited to enterprise, product, medical, and pharma article-to-video workflows that require source-traceable claims, synchronized captions, a visible cover frame, and delivery QA. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-supplied articles or images may include rights-sensitive media or unsupported product and medical claims. <br>
Mitigation: Review article sources, image rights, medical disclaimers, and claim traceability before publishing the generated video package. <br>
Risk: The workflow creates local media project files and relies on FFmpeg/ffprobe and Edge TTS during production. <br>
Mitigation: Run the bundled QA checks, inspect the contact sheet and subtitle synchronization, and deploy only in environments where those media tools and network TTS use are acceptable. <br>


## Reference(s): <br>
- [Content And Compliance](references/content-and-compliance.md) <br>
- [Vertical Layout System](references/layout-system.md) <br>
- [Storyboard And Timeline Schema](references/storyboard-schema.md) <br>
- [Delivery QA](references/qa.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Media files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON production files, and video package deliverables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces storyboard, timeline, voiceover, subtitles, publish copy, QA report, contact sheet, cover image, and MP4 deliverables when the workflow is executed.] <br>

## Skill Version(s): <br>
2.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
