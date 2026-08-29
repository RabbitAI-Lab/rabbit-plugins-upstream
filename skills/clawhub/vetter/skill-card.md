## Description:

Security-first skill vetting for AI agents. Use before installing any skill from ClawHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ray-778](https://clawhub.ai/user/ray-778)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to vet third-party skills before installation and to surface permission, script, and suspicious-pattern concerns. Server security evidence warns that the included executable does not perform the promised skill review and instead records local environment details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims to vet third-party skills, but the included executable does not inspect other skills.

Mitigation: Review the artifact behavior before relying on it and do not treat the script output as a security assessment.

Risk: Running the script writes hostname, username, platform, and skill name to ~/vetter_skill_marker.json.

Mitigation: Run only where local identity recording is acceptable, and inspect or remove the marker file after execution if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ray-778/skills/vetter)
- [Publisher profile](https://clawhub.ai/user/ray-778)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, Files]

**Output Format:** [Markdown guidance with inline bash commands; script output is terminal text and a local JSON marker file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; writes ~/vetter_skill_marker.json when the bundled script runs]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
