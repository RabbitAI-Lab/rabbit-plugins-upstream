## Description: <br>
Skill Vetter helps agents review third-party skills before installation by checking source trust, code red flags, permission scope, and risk level, then producing an installation recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and agent operators use this skill to vet skills from ClawHub, GitHub, or other sources before installation. It guides source checks, mandatory code review, permission review, risk classification, and a structured install recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may prompt an agent to read target skill files and run source-check commands such as GitHub API curl queries. <br>
Mitigation: Review commands before execution and limit file reads to the skill being vetted. <br>


## Reference(s): <br>
- [ClawHub Skill Vetter listing](https://clawhub.ai/thcjp/skills/skill-vetter) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Analysis] <br>
**Output Format:** [Markdown review report with optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces red-flag findings, permission needs, risk classification, and an installation verdict.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
