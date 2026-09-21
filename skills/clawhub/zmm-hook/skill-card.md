## Description:

A Chinese-language short-video opening specialist that first checks whether the content has enough substance, then compares source-material and audience-suspense openings and proposes concise hook candidates with the principle used for each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing assistants use this skill to diagnose whether a short-video topic or draft has enough evidence to support an opening, then generate and compare hook candidates for the first five seconds. It is especially oriented toward solo knowledge creators who need practical, non-jargony opening lines for video scripts or X post first lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags the skill for automatic local or shared memory write-back of user feedback and outcomes.

Mitigation: Install and run it only in a workspace where the referenced memory paths are intentional, and review or disable write-back behavior if persistent notes from content feedback are not desired.

Risk: The skill may read local zmm or vault guidance as part of its Chinese-language writing workflow.

Mitigation: Use it in a dedicated workspace with only the intended guidance files available, and review generated advice before applying it to public content.

Risk: The bundled evaluations are editing exercises and explicitly do not prove click-through, retention, enrollment, or other performance outcomes.

Mitigation: Treat generated openings as editorial candidates and validate them with the publisher's own audience data before relying on performance claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [大众悬念与兑现](artifact/references/大众悬念与兑现.md)
- [规则卡](artifact/references/规则卡.md)
- [zmm-hook 0.4.0 规则演练](artifact/evals/20260914-v0.4.0-规则演练.md)
- [0.4.1 编辑演练](artifact/evals/20260915-v0.4.1-规则演练.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown prose with structured candidate hooks, diagnostic notes, and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Chinese-language hook candidates, principle labels, evidence checks, and requests for missing source material.]

## Skill Version(s):

0.2.10 (source: server release evidence; artifact frontmatter version 0.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
