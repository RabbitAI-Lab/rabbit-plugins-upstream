## Description: <br>
Compresses verbose responses by removing filler and framing to save 200-400 tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to make assistant responses more concise by removing filler, redundant framing, and unnecessary closing text while preserving useful context and safety warnings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Over-compression can remove helpful teaching detail, uncertainty language, or step-by-step setup guidance. <br>
Mitigation: Avoid using the skill for educational explanations, first-time setup, or workflows where careful uncertainty language is important. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-conserve-response-compression) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Concise natural-language or Markdown responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets about 200-400 fewer tokens per verbose response when applicable.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
