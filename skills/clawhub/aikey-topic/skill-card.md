## Description:

AI KEY·今天拍什么 helps single-creator short-video producers explore audience problems, test topic supply and demand, compare evidence, and turn raw ideas into selectable topic candidates instead of one-click topic lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and creator-operators use this skill to evaluate short-video topic ideas, find audience tension, identify evidence gaps, and choose among 3-5 topic candidates with concrete supply-demand reasoning. It is especially oriented toward solo knowledge creators who need topic diagnostics, hooks, positioning checks, and next-step guidance before scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags automatic persistence of user feedback into shared framework and memory files without explicit user approval.

Mitigation: Require explicit user confirmation before any feedback writeback, and prefer a skill-owned memory file over shared framework files that affect other workflows.

Risk: The security guidance notes that the skill may read a content vault and run named local project scripts.

Mitigation: Install only in workspaces where vault access and local script execution are acceptable, and review commands before running them.

Risk: Topic judgments can be misleading if benchmark data, audience demand, or personal evidence is missing or weak.

Mitigation: Keep unsupported claims labeled as inference, verify cited data sources, and treat generated topic candidates as advisory until the creator reviews the evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-topic)
- [问题探寻与共鸣](references/问题探寻与共鸣.md)
- [选题三路](references/选题三路.md)
- [找拉力](references/找拉力.md)
- [常识缺口法](references/常识缺口法.md)
- [规则卡](references/规则卡.md)
- [议程与合集](references/议程与合集.md)
- [Evaluation sample README](evals/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with structured topic candidates, diagnostics, evidence notes, risk notes, next-step options, and occasional shell commands or file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or update local topic pipeline and memory files when the host environment provides the referenced vault and project paths.]

## Skill Version(s):

0.5.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
