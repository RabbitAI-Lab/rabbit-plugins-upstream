## Description: <br>
Creates short, design-led, unnarrated motion graphics, including kinetic type, stats and charts, logo reveals, lower thirds, maps, social/news/web highlights, and image-to-chart asset fusion, rendered as MP4 or transparent overlays. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative agents use this skill to plan, source, build, verify, and render short motion graphics from user-provided content or resolved web/media assets. It is suited to concise brand, data, social, map, UI, news, and asset-fusion animations rather than narrated or multi-scene video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs the agent to silently run a HyperFrames skill update, which can change installed skill behavior without a user review step. <br>
Mitigation: Disable or remove the silent update instruction and require explicit approval before updating installed skills. <br>
Risk: Search-driven categories may source remote assets or use external APIs, including Gemini-assisted localization when keys are available. <br>
Mitigation: Require explicit approval before external uploads or asset searches, freeze selected assets locally, and review the asset provenance ledger. <br>
Risk: Published map or web-asset animations may carry attribution or usage-term obligations. <br>
Mitigation: Review captured asset provenance and map tile terms, and include required attribution in the composition before publishing. <br>


## Reference(s): <br>
- [Builder Contract](references/builder-contract.md) <br>
- [Motion Vocabulary](references/motion-vocabulary.md) <br>
- [Shot Plan IR](references/shot-plan-ir.md) <br>
- [Locate Protocol](grounding/PROTOCOL.md) <br>
- [Source Phase Guide](phases/source/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance, JSON shot plans, HTML/CSS/JavaScript composition files, shell commands, and rendered MP4 or transparent overlay files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are project-local under videos/<project-name>/ and include verification artifacts such as proof snapshots before rendering.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
