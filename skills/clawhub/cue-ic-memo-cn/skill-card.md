## Description:

Drafts a seven-section investment committee discussion memo from company facts or supplied materials, with source locators for figures and explicit notes for missing data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investment analysts and research teams use this skill to prepare source-checkable discussion drafts for pre-investment review. A human reviewer verifies the facts and retains responsibility for ratings and final decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online setup may expose the API key.

Mitigation: Use local drafting without an API key until online setup is reviewed, and do not run the supplied credential-bearing connection examples unchanged.

Risk: The handling of documents sent to Cue is not fully explained.

Mitigation: Approve which documents may be shared and review Cue's privacy terms before submitting them.

Risk: Citation checks have gaps, so unsupported citations or totals may remain in a draft.

Mitigation: Manually verify citations and totals against the original sources.

Risk: Unreviewed dependency versions may introduce unexpected behavior.

Mitigation: Install reviewed dependency versions.

Risk: External services and companion skills were outside this inspection.

Mitigation: Review those services and skills separately before connecting them to sensitive materials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-ic-memo-cn)
- [Cue data tools setup](https://cuecue.cn/hub/mcp)
- [Cue document analysis setup](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [Seven-section Markdown memo, JSON run record, and JSONL source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures include source locators; missing items are listed for human review; the memo is a draft, not an investment decision or recommendation.]

## Skill Version(s):

0.3.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
