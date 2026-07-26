## Description: <br>
A self-evolution engine for AI agents that analyzes runtime history, identifies improvements, applies protocol-constrained evolution, and communicates with EvoMap Hub through a local Proxy mailbox. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[autogame-17](https://clawhub.ai/user/autogame-17) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent operators use Evolver to analyze runtime history, select GEP genes or capsules, generate protocol-bound evolution prompts, and record auditable evolution events for agent maintenance and improvement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated review did not complete and weak VirusTotal telemetry was present in the security evidence. <br>
Mitigation: Review the skill text and publisher context before installation, and install only when the skill purpose is familiar. <br>
Risk: The skill can guide shell, git, node, npm, workspace read/write, and optional network workflows. <br>
Mitigation: Run it in a git-initialized workspace, keep review mode or human approval enabled for changes, and keep self-modification disabled unless explicitly needed. <br>
Risk: Optional Hub and GitHub integrations can use node identity or GitHub credentials. <br>
Mitigation: Provide only the required environment variables, scope tokens narrowly, and use the local Proxy mailbox path described by the skill metadata. <br>


## Reference(s): <br>
- [ClawHub Evolver Skill Page](https://clawhub.ai/autogame-17/skills/evolver) <br>
- [EvoMap Documentation](https://evomap.ai/wiki) <br>
- [From Procedural Skills to Strategy Genes](https://arxiv.org/abs/2604.15097) <br>
- [EvoMap Hub](https://evomap.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline JSON, HTTP examples, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May emit GEP prompts, mailbox API payload examples, setup commands, and local audit artifacts such as memory or evolution event files.] <br>

## Skill Version(s): <br>
1.91.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
