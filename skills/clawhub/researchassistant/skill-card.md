## Description: <br>
Monitors research topics for new papers, conferences, and journals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eksubin](https://clawhub.ai/user/eksubin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to monitor configured research topics and receive concise updates about new papers, conference announcements, and journal publications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics, last check date, and seen paper or URL identifiers are stored locally in research_config.json and may reveal research interests. <br>
Mitigation: Avoid adding confidential research interests and review the local configuration file before deploying or sharing the skill. <br>
Risk: Configured research topics are used in web searches, which may expose those interests to search providers or queried platforms. <br>
Mitigation: Use non-sensitive topic labels and run searches only in environments where that exposure is acceptable. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown research update with concise item summaries and inline script commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local research_config.json with topics, last_checked, and seen_items.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
