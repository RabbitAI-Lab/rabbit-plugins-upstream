## Description: <br>
自动对比2D图纸与3D模型的尺寸、轮廓差异；输出JSON和Markdown格式差异报告；支持直径符号和几何公差识别；适用于设计评审阶段快速发现图纸不一致问题 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and manufacturing engineers use this skill during design review to compare 2D engineering drawings with 3D model geometry and identify dimensional, contour, and tolerance-related differences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reports may include local file paths and design details from provided CAD, PDF, or model files. <br>
Mitigation: Use the skill only on intended project files and review generated reports before sharing them outside the project team. <br>
Risk: Geometric tolerance findings are recorded for review and may require manual measurement validation. <br>
Mitigation: Treat tolerance entries as review prompts and confirm them with engineering judgment or dedicated CAD/metrology tools before making design decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-drawing-diff-analyzer) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-drawing-diff-analyzer) <br>
- [图纸格式指南](references/format-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON feature files and JSON plus Markdown difference reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local 2D drawing and 3D model files, then writes local feature and report files.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
