## Description:

消费 DWG/DXF 或 cad-file-reader 识图产物，输出跨专业碰撞候选和属性冲突清单；2D 图面提示，须人工复核。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

External design and engineering teams can compare structural, architectural, municipal, and MEP drawing data before review to find possible cross-discipline overlaps and attribute conflicts. Treat the results as 2D review candidates and verify them manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags a helper execution-path concern: when run without its dependency path from an untrusted project directory, a helper may run scripts from the current directory.

Mitigation: Review before execution, use trusted project directories, and pass the dependency path explicitly; the normal parent workflow does so.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-clash-check)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Configuration]

**Output Format:** [Machine-readable JSON and human-readable Markdown clash reports, plus JSON and Markdown construction-plan templates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [2D drawing overlap and attribute-conflict candidates for manual review; no 3D BIM collision detection or quantity takeoff.]

## Skill Version(s):

0.3.3 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
