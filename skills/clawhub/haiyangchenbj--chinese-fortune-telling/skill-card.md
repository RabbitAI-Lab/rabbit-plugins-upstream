## Description:

Provides classical-source Chinese fortune-telling workflows that compute BaZi, Zi Wei Dou Shu, divination, compatibility, and date-selection charts with bundled local scripts, then guide the agent to interpret them with stated schools and boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to produce Chinese metaphysics chart readings, divination reports, compatibility analyses, auspicious-date guidance, and checks of third-party fortune-telling reports. The skill is intended for interpretive guidance and excludes medical, legal, and investment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive birth and relationship data.

Mitigation: Collect only the fields needed for the requested reading, explain local-use boundaries before collection, and avoid retaining or sharing the data outside the active task.

Risk: One compatibility script can read local JSON profile files outside its intended profile directory.

Mitigation: Prefer documented direct-input compatibility commands and avoid the two-userId profile mode unless that path-handling issue is fixed.

Risk: Bundled engines require npm dependency installation before use.

Mitigation: Run npm installs in a low-privilege environment and review the package lockfiles before deployment.

Risk: The optional FORTUNE_KNOWLEDGE_DIR override can expand the local files visible to the skill.

Mitigation: Point FORTUNE_KNOWLEDGE_DIR only at a narrow, purpose-built knowledge directory, not broad private folders.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/chinese-fortune-telling)
- [00 · 流派分野与典籍源流](references/00-schools-and-sources.md)
- [01 · 子平格局派](references/01-bazi-geju.md)
- [02 · 调候扶抑派（滴天髓 · 穷通宝鉴）](references/02-bazi-tiaohou.md)
- [03 · 盲派：做功与宾主体用](references/03-bazi-mangpai.md)
- [04 · 紫微斗数](references/04-ziwei.md)
- [05 · 六爻纳甲](references/05-liuyao.md)
- [06 · 梅花易数](references/06-meihua.md)
- [07 · 奇门遁甲](references/07-qimen.md)
- [08 · 大六壬](references/08-daliuren.md)
- [09 · 七政四余](references/09-qizheng-siyu.md)
- [10 · 西方古典占星](references/10-western-classical.md)
- [11 · 择吉（协纪辨方书体系）](references/11-zeri.md)
- [12 · 合婚合盘与流年推断法](references/12-hehun-liunian.md)
- [99 · 断语纪律与红线](references/99-boundaries.md)
- [引擎与桥接脚本命令行用法（engine-usage）](references/engine-usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with local shell commands and structured chart data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local Node scripts to compute charts before producing human-facing readings or reports.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
