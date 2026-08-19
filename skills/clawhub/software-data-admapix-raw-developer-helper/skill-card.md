## Description:

Helps AI-agent users, skill authors, maintainers, and teams produce practical AdMapix-style software and data workflow guidance, including bug-fix support, setup hardening, reliability improvements, checklists, analysis, code, and adjacent-skill planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and AI-agent users use this skill to turn validated demand for AdMapix-style software and data workflows into actionable implementation support, reviews, checklists, and reusable workflow artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation wording is broad enough that an agent could invoke the skill outside a clear AdMapix or raw-data workflow.

Mitigation: Confirm the user request is about AdMapix-style software/data workflows before relying on the skill, and narrow trigger language in a future release.

Risk: Workflow or implementation advice could be incomplete or unsuitable for a user's codebase or data environment.

Mitigation: Require local review, testing, and security scanning before applying generated code, configuration, or process changes.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-admapix-raw-developer-helper)
- [AdMapix Demand Signal](https://clawhub.ai/skills/admapix)
- [Agent Browser Demand Signal](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Ontology Demand Signal](https://clawhub.ai/skills/ontology)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, code snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, validation notes, and remaining risks when helpful.]

## Skill Version(s):

0.20260819.45504 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
