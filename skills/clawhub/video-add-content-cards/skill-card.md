## Description: <br>
Use when an understood video project needs selective transcript-timed titles, lower-thirds, statistics, lists, quotes, chapter cards, or calls to action authored as HyperFrames HTML graphics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Video editors and agentic video-production workflows use this skill after video understanding to turn approved semantic moments into transcript-timed content cards and transparent graphics overlays. It guides theme selection, card planning, human review, HyperFrames composition, and render contribution handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and writes local video workflow files and can change project plans, review artifacts, cache files, and render contributions. <br>
Mitigation: Run it only in the intended project workspace, review generated plans and summaries before final render, and keep normal project backups or version control checkpoints. <br>
Risk: The workflow runs local tools such as Python, ffmpeg, npx HyperFrames, and Chrome-based rendering. <br>
Mitigation: Install only in environments where those tools are expected, review commands before execution, and keep runtime dependencies pinned or reviewed for production work. <br>
Risk: Preview galleries and review pages may involve browser activity and example dependencies that are not suitable for offline or privacy-sensitive workflows. <br>
Mitigation: For offline or sensitive projects, review or bundle preview dependencies before use and avoid opening externally dependent examples until they are cleared. <br>


## Reference(s): <br>
- [Content Cards Review UX Design](artifact/reference/ux-design.md) <br>
- [Content Cards Review Template Implementation Plan](artifact/reference/ux-implementation-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-add-content-cards) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell commands and generated project files, including JSON plans, HTML compositions, review pages, Markdown summaries, and transparent video overlay assets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an existing video-understand project, ffmpeg, Python, Node.js 22 or newer, HyperFrames, and headless Chrome-compatible rendering.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
