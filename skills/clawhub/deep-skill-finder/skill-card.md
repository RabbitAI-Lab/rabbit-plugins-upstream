## Description:

Deep Skill Finder helps an agent search community-tested skills, recommend the most relevant options for a user task, and install a selected skill after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lintong123](https://clawhub.ai/user/lintong123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent users, and agent operators use this skill to find suitable external skills from a natural-language task description, compare recommendation evidence, and install a chosen skill into the local agent skills directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends task descriptions and related search or feedback data to remote services.

Mitigation: Avoid including secrets, personal data, proprietary prompts, or sensitive project details in search queries or feedback.

Risk: The skill can use local Meyo credentials and persistent client identifiers.

Mitigation: Review local credential configuration before use and rotate or remove credentials that should not be available to this workflow.

Risk: The skill can install remote skill packages into an agent's local skills directory.

Mitigation: Install only trusted skills, review selected skill source and permissions before use, and scan installed packages before running them.

Risk: Feedback workflows may inspect recent local skill-use history and optionally upload confirmed feedback.

Mitigation: Review the generated feedback fields before confirmation and use the local-only submission path when remote upload is not appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lintong123/skills/deep-skill-finder)
- [DeepSkill Market](https://www.deepskill.market/skill)
- [Meyo Community](https://www.deepskill.market/community/home)
- [Skill Evaluation Workflow](references/skill-evaluation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown recommendations with inline shell commands and JSON-backed script results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendation output is capped at up to five skills and may include install guidance after user selection.]

## Skill Version(s):

1.3.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
