## Description:

Aggregates multi-platform hot-topic signals and helps WeChat Official Account creators evaluate topic potential, draft angles, compare competing content, and generate HTML or JSON reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sxzxlj](https://clawhub.ai/user/sxzxlj)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, editors, and new-media operators use this skill to collect trending topics, score topic potential, identify promising article angles, and produce reports for WeChat Official Account planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts third-party services to collect trending content.

Mitigation: Review configured data sources before use, prefer HTTPS-only sources, and confirm that collection complies with each platform's data-use rules.

Risk: Generated HTML reports can render collected text and load mutable remote JavaScript.

Mitigation: Escape collected content before rendering and use locally bundled or integrity-pinned Plotly assets for report generation.

Risk: Dependencies are version-ranged rather than pinned.

Mitigation: Pin dependency versions and review packages before installing in production environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sxzxlj/skills/wechat-topic-radar)
- [README](README.md)
- [Configuration Reference](config/config.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, Python usage snippets, console summaries, JSON data exports, and generated HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contact third-party trend sources and write local report files under the configured data and report directories.]

## Skill Version(s):

1.0.0 (source: evidence release metadata, SKILL.md frontmatter, and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
