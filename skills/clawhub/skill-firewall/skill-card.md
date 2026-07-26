## Description: <br>
Security layer that helps agents review external skills for prompt-injection risk and regenerate clean skill text instead of copying untrusted content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mkhaytman87](https://clawhub.ai/user/mkhaytman87) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when reviewing, importing, or rewriting external skills so the agent can identify suspicious patterns and produce a clean replacement for human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger broadly when external skills are discussed, which can add review steps outside an installation or rewrite workflow. <br>
Mitigation: Invoke it when reviewing, importing, or rewriting an external skill, and confirm generated rewrites before saving or deploying them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mkhaytman87/skills/skill-firewall) <br>
- [Project Homepage](https://github.com/openclaw/skill-firewall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code] <br>
**Output Format:** [Markdown with rewritten skill content and approval prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include security review findings and a clean regenerated skill draft.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-02-08) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
