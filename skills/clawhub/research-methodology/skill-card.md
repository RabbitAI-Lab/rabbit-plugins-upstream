## Description:

Guides agents through a Plan-Do-Check-Act research workflow for defining research questions, designing searches, cross-checking sources, and handling conflicting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to structure desk research, industry or competitor analysis, standards research, and evidence-backed research reports. It is intended to keep claims tied to verifiable sources and to flag unresolved source conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording can cause the skill to trigger for general research requests where a narrower methodology prompt may be expected.

Mitigation: Use explicit routing terms such as Research Brief, desk research, source verification, or research methodology when installing or invoking the skill.

Risk: The skill provides methodology guidance rather than automated research execution or independent fact verification.

Mitigation: Require users or downstream agents to verify cited sources, preserve uncertainty labels, and review final research claims before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/research-methodology)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text research plans, source-evaluation notes, and report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multilingual output follows the user's requested or detected language; no executable output or privileged action is defined.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter and manifest list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
