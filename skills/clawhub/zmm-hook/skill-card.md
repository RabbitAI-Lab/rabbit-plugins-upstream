## Description:

Chinese-language skill that diagnoses whether short-video or X-post material has enough substance, then drafts and critiques opening hooks using expectation and information-gap patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to improve the first seconds of Chinese short videos or X posts. It checks whether the underlying content has enough evidence, routes weak material back for more substance, and produces a small set of hook candidates with rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the skill when a user only intended a casual opening-line discussion.

Mitigation: Review configured trigger phrases before deployment and prefer explicit invocation where tighter activation control is required.

Risk: The skill may read and update scoped hook memory, which can preserve user feedback or preferences.

Mitigation: Review memory and writeback behavior before use, and limit or disable local note updates where persistent feedback storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [Publisher profile: iamzifei](https://clawhub.ai/user/iamzifei)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured diagnostics, hook candidates, rationale, and revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically returns concise Chinese-language prose and six grouped hook candidates when the source material passes the gate check.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
