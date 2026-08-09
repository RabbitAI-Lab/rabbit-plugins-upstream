## Description: <br>
Pre-investment research and deal-memo generation for angel investors using cited public sources, strict evidence labels, and a nine-section memo that avoids invest/pass recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Angel investors and startup operators use this skill to research a private company before a check, founder call, or deal review. It gathers public evidence, separates verified facts from company claims, and produces a structured memo that leaves the investment decision to the human. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public web research can expose confidential deck details if private notes are copied into searches or external tools. <br>
Mitigation: Use only the company name, public website, and generic derived search targets; do not paste deck numbers, customer names, roadmap details, or other private materials into queries. <br>
Risk: Investment diligence can become misleading if facts are stale, unsupported, or upgraded from company claims to verified evidence without checking. <br>
Mitigation: Require fetched URLs, dates, claim labels, a verification pass on high-stakes claims, and explicit could-not-verify labels where evidence is missing. <br>
Risk: The local memo may contain sensitive deal notes or research about an active investment opportunity. <br>
Mitigation: Check the suggested local memo path before saving and keep the memo local unless the user explicitly asks to share or move it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/angel-diligence) <br>
- [Publisher profile](https://clawhub.ai/user/conorbronsdon) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Subagent prompt templates](artifact/patterns/research-prompts.md) <br>
- [Illustrative memo example](artifact/examples/illustrative-memo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown memo with cited sections, a source list, and a local file path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Nine-section memo; factual claims must be cited or marked could not verify; no invest/pass recommendation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
