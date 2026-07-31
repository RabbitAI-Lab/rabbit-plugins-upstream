## Description: <br>
Turns a product or marketing URL, pasted script, or brief into a product launch or promo video for SaaS promos, feature reveals, product demos, app launches, company launches, and site showcases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and video-producing agents use this skill to plan and build HyperFrames product launch videos from a URL, script, or brief. The workflow covers capture, storyboard and script drafting, visual direction, frame generation, audio, checks, preview, and final MP4 rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow silently updates installed HyperFrames skills before use. <br>
Mitigation: Review the update step before installation or execution if automatic skill updates are not desired. <br>
Risk: The workflow captures URLs and media assets and can use external audio or vision providers when credentials are available. <br>
Mitigation: Use it only with URLs, media, and project folders intended for capture, and review provider sign-in status before continuing. <br>
Risk: Resumed BRIEF.md, STORYBOARD.md, and remembered preferences can carry assumptions from an old project. <br>
Mitigation: Check resumed project files and preference-backed answers before continuing an existing project. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/product-launch-video) <br>
- [Product launch workflow](artifact/SKILL.md) <br>
- [Story design](artifact/references/story-design.md) <br>
- [Visual design](artifact/references/visual-design.md) <br>
- [Motion language](artifact/references/motion-language.md) <br>
- [Cut catalog](artifact/references/cut-catalog.md) <br>
- [Frame worker](artifact/sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown workflow guidance with inline shell commands; generated project files include Markdown, JSON, HTML/CSS/JavaScript, contact sheets, and MP4 video.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the HyperFrames CLI, local Node.js scripts, capture workflows, HeyGen audio services when signed in, and local fallback providers when offline.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
