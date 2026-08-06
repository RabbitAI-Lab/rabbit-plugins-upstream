## Description: <br>
Helps agents create p5.js algorithmic and generative art with seeded randomness and interactive parameter exploration, while also containing broader automation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative coders can use this skill to request p5.js generative-art guidance, structured inputs and outputs, and parameter-driven creative workflows. Reviewers should account for the broader automation and shell-execution posture described by the security evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is labeled for algorithmic art but includes broader automation guidance that could cause it to activate outside the expected creative-coding scope. <br>
Mitigation: Review intended use before installation and prefer a version that narrows activation to p5.js or generative-art workflows. <br>
Risk: The skill requests shell execution capability, increasing review burden even though no destructive or exfiltration behavior was reported. <br>
Mitigation: Run with least privilege, inspect commands before execution, and use a sandboxed workspace for generated scripts or troubleshooting steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/algorithmic-art) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured examples and optional JSON or shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include p5.js-oriented creative code guidance and broader automation troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
