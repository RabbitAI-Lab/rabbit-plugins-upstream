## Description: <br>
Harness guides agents through stable LLM workflows with pipeline sequencing, guardrail checks, and bounded recovery from verification failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Harness to structure autonomous or headless LLM workflows so intent is clarified, source truth is checked, execution stays in scope, and verification failures are handled with bounded retry or escalation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured pipeline, guard, or recovery receivers can change the actual execution behavior. <br>
Mitigation: Review any custom receivers before deployment and confirm their security posture matches the intended workflow. <br>


## Reference(s): <br>
- [Harness Skill Page](https://clawhub.ai/drumrobot/skills/harness) <br>
- [Pipeline Guide](pipeline.md) <br>
- [Guardrails Guide](guardrails.md) <br>
- [Recovery Guide](recovery.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with structured workflow reports and optional delegated code or shell-command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May delegate planning and implementation to configured pipeline receivers; retry budget defaults to 2.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata, skill frontmatter, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
