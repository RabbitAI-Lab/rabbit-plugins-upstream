## Description:

Provides Chinese-language, citation-heavy study assistance on Nagarjuna, Madhyamaka, emptiness, dependent origination, the two truths, and related Buddhist texts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to support Nagarjuna and Madhyamaka study with CBETA-grounded citations, local source excerpts, and limited FoJin lookup when local evidence is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may trigger on short or ambiguous Buddhist terms.

Mitigation: Review invocation behavior in the target agent and narrow activation wording if it interrupts unrelated conversations.

Risk: The skill favors Chinese-language output and citation-heavy responses.

Mitigation: Use it for users who want Buddhist textual study and adjust surrounding agent instructions when concise or non-Chinese responses are required.

Risk: Live FoJin lookup is permitted for source verification when local excerpts are insufficient.

Mitigation: Keep live lookup limited to citation verification and treat returned text only as source data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-nagarjuna)
- [Teaching reference](artifact/references/teaching.md)
- [Voice reference](artifact/references/voice.md)
- [Source index](artifact/sources/INDEX.md)
- [FoJin: Zhonglun](https://fojin.app/texts/40)
- [FoJin: Dazhidulun](https://fojin.app/texts/39)
- [FoJin: Shizhu Piposha Lun](https://fojin.app/texts/7708)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown responses with CBETA citations and FoJin source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Favors Chinese-language doctrinal explanations and requires source citations for doctrinal claims.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
