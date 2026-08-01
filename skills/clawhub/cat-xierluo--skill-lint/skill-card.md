## Description: <br>
Skill Lint helps agents review skill design, release readiness, harness evidence, instruction stability, directory structure, business-flow coverage, and security risk before or after creating or changing a skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, reviewers, and skill publishers use this skill to assess whether an agent skill is structurally sound, publishable, evaluable, and supported by candidate-bound evidence. It is intended for skill creation prechecks, release reviews, retrofit assessments, third-party skill reviews, and regression checks, not as a replacement for domain validators or general code review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dynamic verification paths may run candidate code. <br>
Mitigation: Use static assessment for unknown third-party skills, and run dynamic verification only for trusted candidates in a disposable or otherwise isolated environment. <br>
Risk: Evidence-signing features can bind unreviewed or attacker-controlled JSON if misused. <br>
Mitigation: Sign only evidence that was created and reviewed by the evaluator, and keep evaluator private keys outside candidate workspaces and away from any process that runs candidate code. <br>
Risk: A security or quality review tool may be over-trusted as a full sandbox or domain validator. <br>
Mitigation: Treat its results as review evidence, keep domain-specific correctness checks separate, and require explicit verification status labels before claiming completion. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cat-xierluo/skills/skill-lint) <br>
- [Project Homepage](https://github.com/cat-xierluo/legal-skills) <br>
- [Skill Standards](references/skill-standards.md) <br>
- [Harness Reliability Standards](references/harness-reliability-standards.md) <br>
- [Instruction Stability Standards](references/instruction-stability-standards.md) <br>
- [Security Assessment Standards](references/security-assessment-standards.md) <br>
- [Workflow Output Standards](references/workflow-output-standards.md) <br>
- [Skill Quality Opinion Report Template](templates/skill-quality-opinion-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown review reports, structured JSON evidence, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce verification status labels such as NOT_VERIFIED, HARNESS_REVIEW_VERIFIED, INSTRUCTION_STABILITY_EVIDENCE_READY, INSTRUCTION_STABILITY_VERIFIED, and DOMAIN_VERIFIED.] <br>

## Skill Version(s): <br>
2.6.1 (source: frontmatter, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
