## Description:

Identifies and removes AI watermarks and provenance marks in user-created or edited images, video, audio, and text, including visible labels and embedded metadata.

This skill is for research and development only.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to inspect or remove AI labels and provenance marks in content they created or are authorized to edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had incomplete coverage and partially analyzed scripts/probe.py.

Mitigation: Review the partially analyzed script and confirm the requested actions stay within the skill's documented scope before execution.

Risk: Removing local provenance marks can be misrepresented as proof that content is human-made, or applied to third-party paid assets.

Mitigation: Limit removal to content the user created or is authorized to change, and do not treat a removed local signal as proof of origin.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project website](https://raiw.cc)
- [Repository listed in release metadata](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command reference](references/commands.md)
- [Installation guide](references/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and shell commands; modified media or text files when removal is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested operation and available detectors; identification reports describe only the signals checked.]

## Skill Version(s):

1.0.22 (source: skill frontmatter; ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
