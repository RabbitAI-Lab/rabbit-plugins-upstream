## Description:

詹明明·开头前五秒 helps single-creator knowledge publishers diagnose whether a short-video or X-post opening has enough substance, then generate and critique opening hooks with labeled principles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to test whether a draft has enough real material for a strong opening, diagnose weak first-five-second hooks, and produce a small set of distinct hook candidates for short videos or X posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to read referenced local framework and memory files, which may expose private drafts, audience context, or business information.

Mitigation: Install only in workspaces where those files are intended to be accessible, and review the referenced paths before using the skill with sensitive content.

Risk: The skill asks the agent to automatically persist user feedback and preference notes.

Mitigation: Review or disable write-back behavior unless the user has opted in and the storage location is appropriate for the information being saved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with diagnostic notes, numbered choices, and candidate hook options.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read referenced local framework and memory files and may save feedback or preference notes when the host agent follows the skill behavior.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
