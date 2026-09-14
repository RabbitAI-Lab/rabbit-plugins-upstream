## Description:

Chinese fortune telling and BaZi chart-reading skill that uses bundled local scripts to compute charts and guides the agent to interpret results against named classical schools and boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for Chinese fortune-telling workflows such as BaZi chart reading, luck-cycle analysis, divination questions, compatibility checks, date selection, and review of third-party fortune-telling reports. The skill is not intended for medical, legal, investment, Tarot, sun-sign horoscope, numerology, or feng-shui layout advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts can read @file inputs, write --out paths, and invoke local script names, which may exceed the minimum local file access needed for a reading.

Mitigation: Run the skill in a sandbox, avoid untrusted script names and paths, and review or patch bridge scripts before installation.

Risk: Generated fortune-telling reports may contain sensitive personal data such as birth time, location, relationship details, and life-event context.

Mitigation: Limit sharing and retention of generated reports, and handle them as sensitive personal data.

Risk: Dependency installation can vary if packages are installed non-reproducibly.

Mitigation: Prefer reproducible dependency installation such as npm ci where lockfiles are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/chinese-fortune-telling)
- [00 · 流派分野与典籍源流](references/00-schools-and-sources.md)
- [01 · 子平格局派](references/01-bazi-geju.md)
- [02 · 调候扶抑派](references/02-bazi-tiaohou.md)
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

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and concise text guidance, with shell commands for local chart-calculation scripts when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state the chosen school, cite bundled reference material, avoid absolute predictions, and treat generated reports as sensitive personal data.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
