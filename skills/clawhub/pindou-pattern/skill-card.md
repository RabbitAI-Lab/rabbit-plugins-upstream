## Description:

生成拼豆图纸（perler bead pattern），将图片或 JSON 像素数据量化为真实拼豆色号，并生成可打印 SVG 图纸、HTML 预览、CSV 物料清单和 JSON 网格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhexin233-ui](https://clawhub.ai/user/zhexin233-ui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn images or structured pixel grids into bead-pattern construction assets with brand-specific color codes and material counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled local Python script reads user-provided image or JSON inputs and writes SVG, HTML, CSV, or JSON outputs.

Mitigation: Run it only on files intended for pattern generation and review --out, --html, --csv, and --json-out paths before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhexin233-ui/skills/pindou-pattern)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with command examples and generated SVG, HTML, CSV, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are written locally to default or user-selected output paths.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
