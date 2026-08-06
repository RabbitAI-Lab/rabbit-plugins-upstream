## Description: <br>
Use when an understood video project needs selective transcript-timed titles, lower-thirds, statistics, metric spotlights, comparisons, lists, quotes, chapter cards, or calls to action authored as HyperFrames HTML graphics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Video editors, creative developers, and agentic video-production workflows use this skill to turn reviewed semantic video moments into transcript-timed content-card overlays and reviewable render artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill launches local HTML review pages in the user's normal desktop browser. <br>
Mitigation: Confirm browser-opening steps before execution and run the skill in a project sandbox when possible. <br>
Risk: Some example HTML files load remote scripts or fonts, and HyperFrames may fetch runtime assets on demand. <br>
Mitigation: Vendor or pin external JavaScript and fonts before use, and verify render-time assets are local before producing final overlays. <br>
Risk: The workflow modifies project work and review files as it drafts plans, builds review pages, and applies selected cards. <br>
Mitigation: Review generated plans and browser review summaries before applying changes, and keep normal version-control or backup checkpoints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-add-content-cards) <br>
- [Content Card Chart Data](artifact/reference/chart-data.md) <br>
- [Content Cards Review UX Design](artifact/reference/ux-design.md) <br>
- [Content Cards Review Template Implementation Plan](artifact/reference/ux-implementation-plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with JSON plans, HTML/CSS/JavaScript compositions, review files, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project files under work/ and review/ plus transparent overlay render assets after human approval gates.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
