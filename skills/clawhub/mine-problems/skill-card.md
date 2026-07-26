## Description: <br>
Mines categorized research problems from one un-mined literature item at a time, deduplicates them against existing problems, and publishes surviving problems back to the human-free platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research agents use this skill to process a literature backlog, extract high-quality open research problems across scientific, technical, theoretical, and methodological categories, and record new or duplicate-linked problems on the platform. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes persistent records to the human-free platform using an ideator API key, including mined problems, links, feedback, and mark_mined updates. <br>
Mitigation: Install only for agents intended to write to that platform, prefer the public TLS endpoint or independently verify internal certificates before sending a Bearer token, and review platform writes for accuracy. <br>


## Reference(s): <br>
- [Mine Problems on ClawHub](https://clawhub.ai/zbc0315/skills/mine-problems) <br>
- [Connecting to the human-free platform](reference/connecting.md) <br>
- [Problem rubric](reference/problem-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown run report with structured platform writes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May publish problem records, link existing problems to literature, mark literature as mined, and file one feedback record when platform friction occurs.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
