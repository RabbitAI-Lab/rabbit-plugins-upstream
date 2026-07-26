## Description: <br>
Test skills via TDD in fresh subagents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to plan baseline, with-skill, rationalization, and regression tests in fresh agent conversations so they can measure skill behavior without priming bias. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Test logs can capture full model responses that may include secrets, private customer data, or sensitive production details. <br>
Mitigation: Use synthetic prompts and sanitized examples, and avoid copying sensitive data into prompts or logs. <br>
Risk: Testing can be biased if evaluation happens in the same conversation where the skill was developed or discussed. <br>
Mitigation: Run baseline, with-skill, rationalization, and regression tests in fresh conversations with identical prompts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-subagent-testing) <br>
- [Source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Testing patterns](modules/testing-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with testing templates and example command/code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No code execution or external tool calls; users may copy full model responses into test logs.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
