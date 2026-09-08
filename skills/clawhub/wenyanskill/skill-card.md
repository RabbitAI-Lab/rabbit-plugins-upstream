## Description:

WenYan converts AI replies into configurable classical Chinese writing styles using JSON style profiles and local Python validation and scoring tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent builders use this skill to make an agent respond in one of eight classical Chinese styles while preserving technical content such as code, commands, file paths, and URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Casual phrases may unintentionally enable or disable the classical Chinese style mode.

Mitigation: Treat style activation and exit as reversible user preferences and honor clear user intent to return to normal replies.

Risk: Persisted local style settings may carry a selected style across later turns.

Mitigation: Reset or disable the persisted state when the user asks to exit the style or when the conversation context changes.

Risk: Stylized language can reduce clarity for technical or factual answers.

Mitigation: Keep code, commands, file paths, and URLs unchanged, and prioritize factual accuracy over literary style.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pondsi/skills/wenyan-engine)
- [README](README.md)
- [Agent integration guide](assets/agents.md)
- [Usage examples](assets/examples.md)
- [Style comparison reference](assets/style-comparison.md)
- [Shared address system](references/shared/address-system.json)
- [Shared taboo words](references/shared/taboo-words.json)
- [Ruya style profile](references/styles/ruya.style.json)
- [Wuxia style profile](references/styles/wuxia.style.json)
- [Sanguo style profile](references/styles/sanguo.style.json)
- [Zhanguo style profile](references/styles/zhanguo.style.json)
- [Shiji style profile](references/styles/shiji.style.json)
- [Baihua style profile](references/styles/baihua.style.json)
- [Shijing style profile](references/styles/shijing.style.json)
- [Chan style profile](references/styles/chan.style.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Styled natural-language replies, Markdown guidance, shell command snippets, and JSON validation or scoring results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 for optional prompt generation, validation, and scoring; code, commands, file paths, and URLs are intended to remain unchanged.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
