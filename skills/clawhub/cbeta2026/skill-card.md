## Description:

大藏经CBETA2026 helps agents retrieve simplified Chinese CBETA Buddhist canon passages and verify citations with CBETA source locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Buddhist canon passages, validate scripture quotations, generate CBETA links, and produce concise answers or deeper research summaries with source locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation answers can become misleading if CBETA knowledge-base results are mixed with outside scholarship or unsupported text.

Mitigation: Ask the agent to clearly separate CBETA-derived citations from any outside scholarship and to state when available material does not cover an answer.

Risk: Document review or editing workflows can affect user-provided local docx files or Tencent Docs content when intentionally invoked.

Mitigation: Only permit local document handling or Tencent Docs actions when the user has intentionally provided documents for review or editing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gouchunlei2-png/skills/cbeta2026)
- [CBETA Online line-level citation example](https://cbetaonline.dila.edu.tw/zh/T46n1939_p0938c04)
- [CBETA Online volume-level citation example](https://cbetaonline.dila.edu.tw/zh/T1939_001)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown answers, research summaries, citation tables, and CBETA links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should separate CBETA knowledge-base citations from outside scholarship when outside sources are explicitly requested.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
