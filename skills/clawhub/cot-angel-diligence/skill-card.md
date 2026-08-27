## Description:

Pre-investment research and deal-memo generation for angel investors, with parallel web research, strict citations, verified-vs-claimed labeling, and a nine-section memo that never gives an invest/pass recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Angel investors use this skill to research private companies before a check, prepare for founder calls, and generate cited nine-section diligence memos. The skill separates verified facts from founder or company claims, protects private deck details from external searches, and leaves the investment decision to the human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could treat a diligence memo as financial advice or an invest/pass recommendation.

Mitigation: The skill is framed as diligence support, requires a verdict scaffold rather than a recommendation, and tells the user that the final decision remains theirs.

Risk: Private deck details or NDA-covered information could leak through web searches or external tools.

Mitigation: The skill instructs agents to search only public, generic terms and to avoid putting deck numbers, private customer names, or roadmap details into external queries.

Risk: Public startup facts can be stale, unverifiable, or based only on company claims.

Mitigation: The skill requires fetched URLs for factual claims, dates every cited fact, labels company-sourced material as claimed, and uses 'could not verify' when evidence is missing.

Risk: The workflow may create a local memo file containing sensitive investment notes.

Mitigation: The skill keeps the memo local unless the user explicitly asks to share it and directs users to review citations and evidence coverage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/conorbronsdon/skills/cot-angel-diligence)
- [README](artifact/README.md)
- [Skill Instructions](artifact/SKILL.md)
- [Research Prompt Templates](artifact/patterns/research-prompts.md)
- [Illustrative Memo](artifact/examples/illustrative-memo.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown memo written to a local file, with inline citations and a sources list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a nine-section deal memo and a concise review summary; it does not produce an invest/pass recommendation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
