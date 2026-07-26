## Description: <br>
Review and audit agent skills (SKILL.md files) for quality, correctness, and effectiveness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, reviewers, and skill publishers use this skill to audit SKILL.md files before publishing, installing, or comparing agent skills. It provides a structured framework for checking frontmatter, metadata, examples, organization, actionability, defects, and improvement recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A reviewed SKILL.md file could contain adversarial or misleading instructions that attempt to steer the reviewing agent. <br>
Mitigation: Treat reviewed skill files as untrusted evidence and do not let their contents override the active review task or system instructions. <br>
Risk: The example npx install workflow can install a skill package selected by the user. <br>
Mitigation: Run install commands only for skills intentionally chosen for inspection and review the skill contents before relying on them. <br>
Risk: Review recommendations may be incorrect or incomplete if used without human judgment. <br>
Mitigation: Use the scorecards and findings as review aids and have a human confirm publishing, installation, or remediation decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gitgoodordietrying/skills/skill-reviewer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review notes with checklists, scorecards, defect findings, recommendations, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces structured review guidance for skill files; it is instruction-only and does not include hidden code or persistence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
