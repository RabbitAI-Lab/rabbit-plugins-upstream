## Description:

Content Repurposing turns recordings and transcripts into an askable digital-human course.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to repurpose supplied recordings, transcripts, talks, and long-form materials into grounded interactive PersonWise courses. It is suited to course creation, refinement, publishing or access changes, and recovery workflows tied to those materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update the PersonWise CLI and open browser OAuth.

Mitigation: Review install, update, and OAuth prompts carefully, and approve only the expected PersonWise action.

Risk: The skill can upload selected materials, consume existing course credits, and change course visibility when requested.

Mitigation: Approve uploads and publishing only when the named files and visibility match the intended course task.

Risk: Repurposed courses could carry forward unsupported or outdated claims from source recordings.

Mitigation: Keep generated course content grounded in supplied materials, label older sources by date, and flag time-sensitive claims for user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-content-repurposing)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create bounded JSON blueprints and invoke PersonWise CLI commands; final course artifacts are produced by the PersonWise service.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
