## Description: <br>
HF Mini provides a local HeartFlow cognitive preprocessor that generates structured cognition data, self-state signals, judgments, and self-correction support for downstream agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to run a local MCP/cognitive engine for structured reasoning, memory/search, emotion and psychology analysis, and decision support before a downstream model responds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local state and automatic repository-mutation behavior can change project state in ways users may not expect. <br>
Mitigation: Try the skill first in a disposable or dedicated repository, and inspect or disable the self-evolution git commit path before regular use. <br>
Risk: Background-service behavior can keep a local MCP engine running beyond a single interaction. <br>
Mitigation: Keep daemon/background mode disabled unless it is explicitly needed, and review daemon status before and after use. <br>
Risk: Code execution and output-rewriting features can affect local execution or downstream responses when enabled. <br>
Mitigation: Keep the code executor disabled unless needed, require explicit authorization for privileged actions, and review generated proposals before applying them. <br>
Risk: Running the skill in sensitive repositories or directories can expose more local state than intended. <br>
Mitigation: Avoid giving it sensitive project directories or credentials, and use a constrained workspace for evaluation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/hf-mini-test-650) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact security advisory](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured text/tool responses with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cognitive summaries, status fields, proposed code/configuration changes, and local execution guidance; privileged behavior should remain explicitly authorized.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 6.0.36) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
