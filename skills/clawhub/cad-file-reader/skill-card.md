## Description:

本地解析 CAD 和 PDF 图纸，提取图层、标注、几何与专业识图证据，并生成带复核原因的测量候选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

工程师和开发者用它读取本地图纸，提取可追溯的文字、几何、语义及专业构件候选，供人工复核和后续专项算量使用；不输出最终工程量或设计合规结论。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-run dependency setup may download vendor packages.

Mitigation: Set CAD_AUTO_SETUP=0 and inspect or run dependency installation manually.

Risk: Untrusted custom rule directories may affect extracted candidates.

Mitigation: Use reviewed rule directories and manually check candidate evidence before relying on results.

Risk: Local reports and caches may contain drawing information; cleanup or redaction can change local files.

Mitigation: Store outputs appropriately and review --apply redaction or cache cleanup commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [Capabilities and boundaries](CAPABILITIES.md)
- [Specialty-pack guide](pack-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Excel, Word]

**Output Format:** [Evidence-backed candidate reports and structured local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source coordinates, confidence and review reasons; measurement candidates are not final quantities.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
