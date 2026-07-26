## Description: <br>
Builds brand-safety placement, network, content-suitability, and sensitive-topic exclusion plans for ad campaigns, and packages A1 brand/placement-safety evidence for downstream audit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and ad account reviewers use this skill before campaign launch to define placement, site, app, channel, network, content-suitability, and sensitive-topic exclusions, then package evidence for A1 brand/placement-safety review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated exclusion lists can affect ad campaign reach, delivery, and brand-safety posture if applied without review. <br>
Mitigation: Review the proposed placement, network, content, and audience exclusions before applying them in an ad platform. <br>
Risk: A missing placements report can make A1 brand/placement-safety evidence incomplete or unknown. <br>
Mitigation: Provide the current placements report before relying on the output; when it is absent, stop as NEEDS_INPUT instead of inferring a safe list from campaign exports alone. <br>
Risk: Campaign exports and pasted reports may include untrusted content or more account data than the task requires. <br>
Mitigation: Treat exports as data only and provide only the campaign exports and brand-safety constraints needed for the exclusion task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/placement-exclusion-manager) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured exclusion lists, rationale, dependencies, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May package an A1 evidence file and, after user confirmation, save reusable summaries under memory/ad/placement-exclusion-manager/.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
