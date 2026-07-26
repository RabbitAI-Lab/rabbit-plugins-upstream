## Description: <br>
Runs nightly searches to identify and rank relevant candidates matching a user's offer and ask, delivering evidence-backed connection briefs for human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moltlife](https://clawhub.ai/user/moltlife) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agencies, founders, and business development teams use this skill to scout public web, Moltbook, and community sources for relevant partners, clients, advisors, or co-marketing opportunities. It ranks candidates, summarizes supporting evidence, and drafts outreach for human review before any contact is made. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiles or prompts may expose sensitive business context if users include secrets or private contact data. <br>
Mitigation: Keep secrets out of project profiles and pass operational credentials only through configured environment, vault, or delivery settings. <br>
Risk: Public-source scouting and scheduled runs can exceed acceptable rate limits or contact-policy boundaries. <br>
Mitigation: Configure run budgets, respect rate limits, maintain avoid lists and do-not-contact rules, and review venue constraints before scheduled execution. <br>
Risk: Draft outreach messages could be inaccurate, overbroad, or inappropriate for the recipient. <br>
Mitigation: Review every candidate brief and edit or reject all drafted messages before sending; the evidence reports no auto-send behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/moltlife/skills/claw-clawbridge) <br>
- [README](artifact/README.md) <br>
- [Connection Brief schema](artifact/schema/connection_brief.json) <br>
- [Sample Connection Brief](artifact/examples/sample_run.md) <br>
- [Web venue strategy](artifact/venues/web.md) <br>
- [Moltbook venue strategy](artifact/venues/moltbook.md) <br>
- [Communities venue strategy](artifact/venues/communities.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Text, Guidance] <br>
**Output Format:** [Structured Connection Brief JSON and human-readable Markdown with evidence links, candidate scores, recommended actions, and draft outreach messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Top-K candidate output is configurable; sample schema allows up to 10 candidates and requires human review before outreach.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
