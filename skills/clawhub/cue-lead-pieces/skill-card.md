## Description:

使用 Cue Omni Reader 或本地解析公司公开披露，整理带来源页码的信用线索，并逐句核对引文；可修正页码、恢复原文或移除无依据的引文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and researchers can use the skill to review public company filings, organize traceable credit signals, and check quoted text against its cited source pages. Its output is not investment or credit advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed.

Mitigation: Wait for the credential-destination fixes before using real keys, and keep credentials in your own credential store.

Risk: File operations could overwrite data outside the selected folder.

Mitigation: Restrict filesystem access to the intended company data folder and use trusted filing lists.

Risk: An automatic quotation repair could leave a financial amount or claim incorrect.

Mitigation: Manually check amounts and original filing pages after automatic repairs.

Risk: Optional model configuration sends excerpts to the selected provider.

Mitigation: Use this option only with a provider approved for the disclosure excerpts you submit.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-lead-pieces)
- [Cue Omni Reader configuration](https://cuecue.cn/hub/omni-reader)
- [Cue data-MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [Skill instructions](artifact/SKILL.md)
- [Verification notes and limitations](artifact/references/verification.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown credit-signal reports and JSON quotation evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source identifiers and page references; automated quote repairs need review against the original filing.]

## Skill Version(s):

0.4.34 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
