## Description: <br>
Audits Claude and Agent SKILL.md packages for trigger quality, length, progressive disclosure, script extraction, portability, and hard-coded secret risks, then returns a scorecard and prioritized repair guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to audit Agent Skill/SKILL.md directories before publishing, installing, or refactoring them. It combines local deterministic checks with qualitative review to produce scorecards, JSON reports, and prioritized remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit findings and proposed repairs may be incomplete or misleading if treated as a guarantee of skill quality or security. <br>
Mitigation: Use the report as triage, review the target skill before deployment, and re-run checks after changes. <br>
Risk: The optional trigger-evaluation workflow can make paid Claude CLI calls using the user's account. <br>
Mitigation: Run trigger evaluation only when needed, review the query set and expected cost first, and use the zero-dependency check.py workflow as the default path. <br>
Risk: The tool's credential checks should not be assumed to cover every possible credential-named text file or secret pattern. <br>
Mitigation: Keep secrets out of skill packages, scan with an appropriate security process, and manually review sensitive files before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill) <br>
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill) <br>
- [Trigger evaluation guide](references/trigger-eval.md) <br>
- [Skill writing vocabulary](references/skill-writing-vocab.md) <br>
- [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, code, guidance] <br>
**Output Format:** [Markdown scorecards with optional JSON reports and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local Python checks; optional trigger evaluation can invoke the Claude CLI and incur user API costs.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata, SKILL.md frontmatter, changelog released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
