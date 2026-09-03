## Description:

詹明明·开头前五秒 helps agents diagnose whether a short-video or X-post opening has enough substance, then generate concise hook candidates with the principle behind each candidate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing agents use this skill to check whether a proposed opening has enough real material, diagnose weak first-five-second hooks, and draft labeled alternatives for short videos or X posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to read ZMM vault materials that may contain private writing context or preferences.

Mitigation: Install it only in workspaces where the agent is allowed to access those vault materials, and narrow triggers if accidental activation would expose sensitive context.

Risk: The skill asks the agent to save feedback and update shared writing-framework or memory files automatically.

Mitigation: Require confirmation before memory or framework writes, especially in shared repositories or shared vaults.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with gate-check diagnostics and grouped hook candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically includes substance checks, labeled hook principles, concise revision guidance, and a next-step choice when more input is needed.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
