## Description: <br>
Create a production-ready chibi pixel-art virtual desktop pet based on a character reference image, including character design sheets, multi-action animation sprite sheets, transparent RGBA frame assets, action strips, asset inventories, GIF previews, automatic character alignment using alpha edges and connected-component analysis, jitter measurement, asset validation, ZIP packaging, and web integration delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mmgongzhu](https://clawhub.ai/user/mmgongzhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, game creators, and agent users use this skill to turn character references into aligned pixel-pet sprite packages or repair existing transparent sprite packages with animation drift. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image generation and iterative sprite creation can consume tokens or provider quota. <br>
Mitigation: Plan character design, action counts, frame counts, and generation phases before starting; generate incrementally and reuse approved masters. <br>
Risk: Packaging and alignment commands write local sprite assets and ZIP exports to requested output paths. <br>
Mitigation: Review output directories before running commands and rely on versioned sibling outputs rather than overwriting existing assets. <br>
Risk: Generated frames may drift, clip, or fail transparency and edge-quality checks. <br>
Mitigation: Run the included alignment and validation scripts before delivery and regenerate or add transparent padding when clipping prevents clean alignment. <br>


## Reference(s): <br>
- [Package configuration](references/package-config.md) <br>
- [Pixel-pet prompt patterns](references/prompting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration examples, file paths, and QA summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local sprite package artifacts such as transparent RGBA frames, atlases, strips, GIF previews, manifests, validation reports, and ZIP exports when its workflow is executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
