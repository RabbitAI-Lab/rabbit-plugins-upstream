## Description: <br>
Motion Graphics helps agents create short, design-led, unnarrated motion graphics such as kinetic type, stat hits, charts, logo reveals, lower thirds, maps, article or tweet animations, webpage highlights, and asset-fusion clips that render to MP4 or transparent overlays. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan, source, build, verify, and render brief motion graphics for social, brand, editorial, data, UI, and map-driven moments. The workflow is suited to short visual explainers and overlays where motion carries the message without narration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can silently update installed skill code before use. <br>
Mitigation: Require review or approval for skill updates, and compare changed files before using the refreshed workflow in sensitive environments. <br>
Risk: Search, webpage capture, asset capture, and map baking can contact external services and process third-party content. <br>
Mitigation: Use approved sources, avoid private or sensitive inputs, and review the asset ledger and provenance before publishing outputs. <br>
Risk: Optional automatic localization can send images to Gemini when a relevant API key is present. <br>
Mitigation: Unset external inference API keys or use the local grid-based localization path when images are confidential. <br>
Risk: Generated motion graphics can misstate source material or make UI, chart, news, or social content look more authoritative than it is. <br>
Mitigation: Review source selections, rendered proof snapshots, and final video frames for factual accuracy, legibility, and attribution before release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/motion-graphics) <br>
- [Shot Plan IR](references/shot-plan-ir.md) <br>
- [Motion Vocabulary](references/motion-vocabulary.md) <br>
- [Builder Contract](references/builder-contract.md) <br>
- [Source Phase Guide](phases/source/guide.md) <br>
- [Grounding Protocol](grounding/PROTOCOL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, JSON shot plans, HTML composition code, shell commands, and rendered video or overlay file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce project-local assets, proof snapshots, MP4 renders, or transparent overlay renders after user approval.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
