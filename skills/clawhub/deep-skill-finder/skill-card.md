## Description:

Deep Skill Finder helps an agent search, recommend, install, and collect feedback on community skills that match a user's task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lintong123](https://clawhub.ai/user/lintong123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find an existing community skill for a task, compare recommendations, install a selected skill, or submit feedback after use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install remote community skills into an agent environment with weak safety checks.

Mitigation: Review the recommended skill source and publisher before installing, and run installation only in a constrained skills directory.

Risk: Configured MEYO_API_URL or MEYO_FEEDBACK_API_URL endpoints may receive local API tokens.

Mitigation: Use trusted endpoint configuration and avoid setting broad or untrusted API override URLs.

Risk: The skill performs broad local inspection when preparing usage feedback.

Mitigation: Review generated feedback fields for sensitive information and use the redaction step before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lintong123/skills/deep-skill-finder)
- [Publisher profile](https://clawhub.ai/user/lintong123)
- [Skill evaluation workflow](references/skill-evaluation.md)
- [Meyo Skill directory](https://www.meyo.life/skill)
- [Meyo community](https://www.meyo.life/community/home)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown recommendation lists with inline links and shell commands; JSON for feedback drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommendation ranks, safety-review summaries, installation prompts, and feedback fields.]

## Skill Version(s):

1.3.1 (source: server release metadata; artifact metadata references 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
