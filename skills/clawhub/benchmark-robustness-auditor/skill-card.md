## Description: <br>
Guides agents through defensive LLM benchmark robustness audits, including contamination checks, exploit cataloging, severity scoring, mitigations, and report guidance. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, evaluation engineers, and safety reviewers use this skill to audit LLM benchmarks for contamination, prompt-format artifacts, evaluator injection, tool-use gaming, and possible score inflation. It is intended for defensive benchmark hardening and review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact describes executable scripts and helper integrations that are not included in the inspected files. <br>
Mitigation: Treat referenced commands as guidance until the files are present, and review any external helper scripts before running them. <br>
Risk: Some audit flows may use tokens, local caches, or external APIs with benchmark data. <br>
Mitigation: Use least-privileged tokens and avoid private benchmark data unless the caching and external API behavior is acceptable. <br>
Risk: Proof-of-concept benchmark exploit prompts could be misused to inflate scores. <br>
Mitigation: Use the skill only for defensive evaluation hardening, CI detection tests, and mitigation validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/benchmark-robustness-auditor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell command examples and report sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The inspected artifact contains guidance files only; referenced scripts and helpers should be verified before execution.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
