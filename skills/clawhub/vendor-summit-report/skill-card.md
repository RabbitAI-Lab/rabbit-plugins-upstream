## Description:

Builds executive-oriented deep-dive reports for major data and AI vendor conferences, producing aligned HTML, Markdown, and enterprise-chat deliverables with analyst-style structure, caveats, buyer recommendations, and confidence-tagged planning assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and enterprise strategy teams use this skill to turn a named vendor summit into an executive-grade conference report with fresh research, buyer recommendations, caveats, and synchronized HTML, Markdown, and enterprise-chat outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conference facts, customer metrics, product availability, and competitive claims can be wrong, stale, or vendor-reported.

Mitigation: Review the generated facts, source dates, caveats, and language before sharing the report, and verify important figures against primary sources or buyer workloads.

Risk: The workflow creates local deliverables that may later be published or pushed to a live channel.

Mitigation: Confirm the destination and inspect the HTML, Markdown, and enterprise-chat outputs before any live publish or push action.

Risk: The three deliverables can drift if a revision updates only one format.

Mitigation: Run the documented cross-file consistency check so figures, cases, caveats, and section numbering match across all outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/vendor-summit-report)
- [README](artifact/README.md)
- [Skill workflow](artifact/SKILL.md)
- [HTML report template](artifact/templates/report-template.html)
- [Markdown report template](artifact/templates/report-template.md)
- [Enterprise-chat template](artifact/templates/wecom-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [HTML, Markdown, and plain-text enterprise-chat deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates three aligned local deliverables and requires fact, caveat, and section-consistency checks before delivery or publishing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
