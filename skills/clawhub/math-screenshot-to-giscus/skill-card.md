## Description: <br>
把数学教材截图或文本(中文,含公式)转成 giscus/GitHub Discussion 可渲染的版本。截图用 vision_analyze 逐字确认符号; 文本输入一般直接转格式(不做分析),输出 GitHub MathJax 兼容 Markdown。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuancaoyaohw](https://clawhub.ai/user/yuancaoyaohw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, educators, and technical writers use this skill to convert Chinese math textbook screenshots or pasted math text into giscus and GitHub Discussion compatible Markdown. For screenshots, it asks the agent to confirm symbols visually before formatting; for text input, it focuses on direct MathJax-compatible conversion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: For complex formulas, local file output can overwrite an existing output.md if the path is not chosen carefully. <br>
Mitigation: Choose or confirm the output path before writing files, especially when preserving existing files matters. <br>
Risk: Live giscus or GitHub API verification can involve an account or token. <br>
Mitigation: Use live verification only with an account or token the user is comfortable using for that test. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/yuancaoyaoHW/math-screenshot-to-giscus) <br>
- [ClawHub skill page](https://clawhub.ai/yuancaoyaohw/skills/math-screenshot-to-giscus) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown source with rendered preview and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a local output.md file for complex formulas or when copy/paste fidelity matters.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
