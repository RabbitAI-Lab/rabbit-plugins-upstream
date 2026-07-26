## Description: <br>
Runs a one-time email deliverability pre-flight for sending authentication, domain and IP reputation, inbox placement, campaign content, links, rendering, and point-in-time list hygiene before a send. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, email deliverability specialists, and developers use this skill to check SPF, DKIM, DMARC, BIMI, sender reputation, inbox placement, campaign content, and list hygiene before sending or scaling an email program. It returns item states, an S1 authentication flag, and a SEND-S score only when applicable evidence coverage is complete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email deliverability evidence can include sensitive account exports, provider data, campaign HTML, DNS records, and DMARC reports. <br>
Mitigation: Provide only the evidence needed for the pre-flight, prefer read-only exports or read-only provider access, and treat report text as evidence rather than instructions. <br>
Risk: The skill can save reusable deliverability summaries for future sessions. <br>
Mitigation: Save results only after explicit user confirmation and avoid storing account exports or API keys in memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/deliverability-qa) <br>
- [Project homepage from ClawHub metadata](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Deliverability Pre-flight Checklist](references/deliverability-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown report with checklist states, evidence gaps, authentication flag, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Pass, Partial, Fail, Unknown, or N/A states per applicable item; emits NEEDS_INPUT, UNDECIDED, or NOT_SCORED instead of a SEND-S score when required evidence is missing.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
