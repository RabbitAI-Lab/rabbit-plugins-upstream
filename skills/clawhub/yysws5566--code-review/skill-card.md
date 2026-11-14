## Description:

AI 写的代码敢直接用吗？交给它审：出一份人话体检清单——哪里有坑、不修会怎样、先修哪个，每条都写到你看得懂，不懂代码也能拍板。只出清单不动手改，防止越改越乱。触发词：review代码、代码审查、代码体检、把关代码、上线前检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yysws5566](https://clawhub.ai/user/yysws5566)

### License/Terms of Use:

MIT-0

## Use Case:

Individual developers and people reviewing AI-generated code use this skill to inspect a file, project, or diff across seven review dimensions and receive a severity-ranked checklist in plain language. It keeps review findings separate from code changes and marks conclusions that still need verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review workflow may execute code from the project being reviewed, which can undermine the promised read-only review.

Mitigation: Before allowing execution during review, inspect and isolate the project code and decide whether running it is acceptable; use static checks when execution is not acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yysws5566/skills/code-review)
- [Publisher profile](https://clawhub.ai/user/yysws5566)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown code-review checklist ranked by severity, with file and line locations, plain-language impact, evidence status, and suggested priority.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review findings are presented as a checklist; the skill separates review from making code changes.]

## Skill Version(s):

1.2.3 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
