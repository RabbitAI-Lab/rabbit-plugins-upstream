## Description:

给定决策主体与竞品清单，本技能先构建逐条带来源、日期及 fact、inference 或 opinion 标注的证据表，再据此生成一页内的建议简报并列明证据覆盖缺口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

市场与产品团队可围绕一项决策比较指定竞品，生成能逐条追溯来源的简报；不适用于法律结论或推断非公开信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Cue connection setup has incomplete protections that could expose the API key.

Mitigation: Use the supplied-material workflow without a Cue key until authenticated examples validate destinations and the helper disables or safely revalidates redirects.

Risk: Uploading local documents can disclose sensitive competitive or internal information.

Mitigation: Approve each local-document upload separately and review optional dependencies; pin installation versions where possible.

Risk: A checker pass verifies formatting, not the truth or traceability of claims.

Mitigation: Review each claim against its cited source and check the stated evidence coverage and gaps.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-competitive-brief)
- [Cue onboarding guide](references/cue-onboarding.md)
- [Evidence standards](references/evidence-standards.md)
- [Cue MCP configuration](https://cuecue.cn/hub/mcp)
- [Omni-reader configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown evidence table and concise decision brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims include source, date, and evidence level; coverage and unfilled dimensions are reported.]

## Skill Version(s):

0.3.33 (source: SKILL.md frontmatter, CHANGELOG, released 2026-10-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
