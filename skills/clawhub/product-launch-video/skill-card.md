## Description: <br>
Turns a product or marketing URL, pasted script, or brief into a product launch or promotional video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and creative operators use this skill to capture product context, plan a launch story, build HyperFrames HTML compositions, and render a promotional MP4 for product reveals, SaaS promos, demos, site showcases, and company launches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can run a networked self-update that changes installed skills or shared HyperFrames dependencies before user approval. <br>
Mitigation: Review the release before installation and use an explicit update policy so dependency or skill updates are deliberate and auditable. <br>
Risk: The workflow uses network services for product capture and media retrieval, including voice, music, and sound-effect paths when credentials or providers are available. <br>
Mitigation: Use offline or signed-out paths when appropriate, provide only scoped credentials, and avoid sending sensitive product URLs, assets, or briefs to network services unless approved. <br>
Risk: Generated HTML may load GSAP from jsDelivr unless changed. <br>
Mitigation: Review generated HTML before deployment and vendor, pin, or allowlist external browser dependencies according to the target environment's policy. <br>


## Reference(s): <br>
- [Product Launch Video ClawHub listing](https://clawhub.ai/heygen-com/skills/product-launch-video) <br>
- [Story design](references/story-design.md) <br>
- [Visual design](references/visual-design.md) <br>
- [Motion language](references/motion-language.md) <br>
- [Cut catalog](references/cut-catalog.md) <br>
- [Frame worker](sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown plans and scripts, JSON metadata, shell commands, HTML frame compositions, caption/audio artifacts, and rendered video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are project-scoped under videos/<project>; the workflow may create hyperframes.json, BRIEF.md, STORYBOARD.md, SCRIPT.md, frame.md, audio_meta.json, caption_groups.json, compositions/frames/*.html, index.html, snapshots, and renders/video.mp4.] <br>

## Skill Version(s): <br>
1.0.18 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
