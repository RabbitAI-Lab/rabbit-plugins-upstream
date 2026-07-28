## Description: <br>
clawvet is a code quality and safety linter that runs six analysis passes to catch prompt injection, credential theft, and remote-code-execution risks in OpenClaw skills before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohibshaikh](https://clawhub.ai/user/mohibshaikh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to scan OpenClaw skill directories before installation, audit installed skills, and produce CI-friendly safety results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented npx commands run an npm-distributed CLI on local skill directories. <br>
Mitigation: Review the package source and run scans in a controlled workspace before using it on sensitive skill repositories. <br>
Risk: Audit and watch features read local OpenClaw skill directories, and optional features can use network access. <br>
Mitigation: Use least-privilege working directories and leave optional telemetry or network-backed analysis disabled unless needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet) <br>
- [Project repository](https://github.com/MohibShaikh/clawvet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm; optional semantic analysis can use user-provided Anthropic, OpenAI, Zhipu, or local Ollama credentials.] <br>

## Skill Version(s): <br>
0.9.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
