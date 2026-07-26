## Description: <br>
Automates desktop GUI workflows via computer use API with screenshot capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to direct an agent through GUI workflows that require screenshots, mouse and keyboard actions, visual testing, form filling, or desktop-app navigation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Desktop automation can interact with sensitive accounts, private data, or workflows with real-world consequences. <br>
Mitigation: Run the skill in a sandbox or VM, avoid sensitive accounts and banking, and require human confirmation before consequential actions. <br>
Risk: Screenshots can expose private information visible on the desktop. <br>
Mitigation: Close sensitive apps and use a limited desktop session before giving the agent screenshot access. <br>
Risk: Long-running computer-use loops can repeat unwanted actions or increase API cost. <br>
Mitigation: Set iteration limits and stop the session when the task is complete or behavior diverges from the requested workflow. <br>


## Reference(s): <br>
- [Phantom plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/phantom) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include environment setup commands, model and tool-version guidance, and safety constraints.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
