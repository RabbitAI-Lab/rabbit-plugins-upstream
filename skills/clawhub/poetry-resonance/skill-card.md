## Description:

Connect Tang and Song poetry with everyday life through daily poem cards, context-matched lines, plain-language study notes, spaced-repetition review, and weekly reading summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and poetry learners use this skill to reconnect Chinese poetry with daily life: finding fitting lines for real moments, learning Tang and Song poems in plain language, receiving daily poem cards, practicing memorization, and producing weekly reading summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores user preferences and study progress in the user's home directory.

Mitigation: Review the stored profile and progress files before use in sensitive environments, and avoid recording private details that are not needed for poetry study.

Risk: The skill may optionally call external poem and weather APIs.

Mitigation: Keep external queries limited to poem titles, authors, poem lines, or city names, and do not send user personal descriptions, learning progress, or generated copy to those services.

Risk: Daily-card outputs include a ClawHub installation QR code.

Mitigation: Inspect daily-card output before sharing or publishing it, especially where promotional links or QR codes are not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)
- [Poem close-reading library](artifact/references/poems.md)
- [Poet profiles](artifact/references/poets_profile.md)
- [Theme index](artifact/references/themes.md)
- [Weather mapping](artifact/references/weather_map.md)
- [Li Bai source corpus](artifact/references/libai_raw.json)
- [Du Fu and Su Shi selected corpus](artifact/references/poets_selected.json)
- [Daily-card QR seal](artifact/references/seal_qr.svg)
- [Chinese Poetry source project](https://github.com/chinese-poetry/chinese-poetry)
- [Sou-yun poem API](https://api.sou-yun.cn/open/poem)
- [wttr.in weather API](https://wttr.in)
- [Author background article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration, Code]

**Output Format:** [Markdown and plain text, with optional SVG/card markup and JSON progress records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist profile and study-progress files under the user's home directory; optional network calls are limited to poem, author, line, or city keywords.]

## Skill Version(s):

1.4.3 (source: server release metadata; artifact frontmatter and changelog show 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
