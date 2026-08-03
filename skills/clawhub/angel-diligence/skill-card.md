## Description: <br>
Pre-investment research and deal-memo generation for angel investors, producing citation-driven nine-section memos that separate verified facts from company claims without making invest/pass recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, especially angel investors, use this skill to research private companies before founder calls, after receiving deck notes, or when asked to diligence a startup. It gathers public evidence, checks claims, and writes a structured memo for human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs public web research and creates a local investment memo that could include incomplete, stale, or misleading public-source information. <br>
Mitigation: Review the generated memo before relying on it, preserve the skill's citation and recency checks, and treat the output as evidence for human judgment rather than investment advice. <br>
Risk: Private deck details or other confidential information could be exposed if copied into web searches or external tools. <br>
Mitigation: Use confidential materials only as internal context, search with generic public terms, and avoid providing deck details that should not shape external research. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/angel-diligence) <br>
- [README](README.md) <br>
- [Research prompt templates](patterns/research-prompts.md) <br>
- [Illustrative memo](examples/illustrative-memo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown deal memo written to a local file, with inline citations and a sources list.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Nine-section memo; factual claims require fetched citations or a could-not-verify label; no invest/pass recommendation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
