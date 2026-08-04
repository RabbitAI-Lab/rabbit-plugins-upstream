## Description: <br>
Guide creating Claude Code skills with TDD and persuasion principles. Use for new skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create and validate Claude Code skills with test-driven development, progressive disclosure, description tuning, anti-rationalization patterns, and deployment quality gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes deployment and validation command examples that an agent may propose during skill authoring. <br>
Mitigation: Review commands before execution and run them only in the intended repository and permission context. <br>
Risk: Skill testing workflows may capture transcripts, test prompts, or example files that include sensitive material. <br>
Mitigation: Use sanitized test cases and avoid storing private transcripts, credentials, customer data, or proprietary code in skill test files. <br>
Risk: Broad trigger terms may cause the skill to activate outside its intended skill-authoring context. <br>
Mitigation: Narrow activation triggers during installation or maintenance when the deployment environment supports trigger tuning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-authoring) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [TDD Methodology](modules/tdd-methodology.md) <br>
- [Persuasion Principles](modules/persuasion-principles.md) <br>
- [Progressive Disclosure](modules/progressive-disclosure.md) <br>
- [Skill Validation](modules/validation.md) <br>
- [Deployment Checklist](modules/deployment-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline examples, command snippets, checklists, and configuration patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only skill guidance; no direct execution behavior is bundled.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
