## Description: <br>
Render Blender files with agent-controlled procedural parameters for synthetic data generation, returning Naturalness, LPIPS, and dataset diversity metrics to help agents optimize parameter ranges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ayakimovich](https://clawhub.ai/user/ayakimovich) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and ML engineers use SynthClaw to analyze Blender scenes, adjust named procedural Value Nodes, render single images or datasets, and evaluate generated outputs with quality and diversity metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-supplied Blender files can execute in the normal environment during rendering. <br>
Mitigation: Use trusted .blend files and run the skill in a low-privilege or sandboxed environment without sensitive environment variables. <br>
Risk: Dataset cleanup may remove TIFF files inside the selected output directory. <br>
Mitigation: Use a fresh, dedicated output directory for each dataset render and avoid pointing the skill at directories containing files that must be preserved. <br>
Risk: Rendering before scene discovery can target the wrong procedural controls or produce unusable outputs. <br>
Mitigation: Run analyze_blend before rendering so the agent uses the discovered Value Node, material, object, and collection names. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ayakimovich/skills/synthclaw) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, json, guidance] <br>
**Output Format:** [JSON responses with rendered image or dataset file paths, logs, scene analysis, and optional quality metrics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated artifacts may include PNG renders, dataset folders, compositor outputs, and per-image metric summaries.] <br>

## Skill Version(s): <br>
0.2.6 (source: SKILL.md frontmatter, pyproject.toml, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
