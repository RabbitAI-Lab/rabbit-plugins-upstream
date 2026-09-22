## Description:

詹明明·开头前五秒 helps agents diagnose whether a short-video or X-post opening has enough source material, compare material-led and audience-suspense entry points, and produce annotated hook candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this Chinese-language skill to test whether a draft has enough evidence for a strong opening, choose an opening route, and draft hook candidates with concise rationale. It is especially focused on short-video first-five-seconds openings and X-post first lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local zmm/vault writing references and save hook-related preferences when those paths are available.

Mitigation: Review the memory and draft writeback behavior before installation, and run it only in workspaces where those persistent edits are acceptable.

Risk: Generated hooks can overpromise if the source draft lacks evidence for the opening's claim.

Mitigation: Review each candidate against the supplied draft and keep only openings whose promised evidence can be delivered in the body.

## Reference(s):

- [大众悬念与兑现](artifact/references/大众悬念与兑现.md)
- [规则卡](artifact/references/规则卡.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown prose with diagnostic bullets and grouped hook candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local writing memory and save hook-related preferences when the agent environment provides that workspace.]

## Skill Version(s):

0.2.11 (source: server release metadata; artifact frontmatter reports 0.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
