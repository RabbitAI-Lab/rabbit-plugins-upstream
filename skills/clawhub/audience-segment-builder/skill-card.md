## Description: <br>
Builds paid-ad audience segment plans from authorized customer, CRM, ecommerce, or GA4 exports, including seed audiences, value-based lookalike seed lists, suppression segments, and platform-neutral funnel maps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, growth, and advertising teams use this skill to turn their own exported customer or analytics data into named paid-ad audiences, lookalike seed definitions, exclusions, and funnel-stage targeting maps. It helps prepare who to target or suppress before campaign structure and match-type work begins. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process customer, CRM, ecommerce, or GA4 exports containing personal or commercially sensitive data. <br>
Mitigation: Use only data the user is authorized to process and keep saved outputs to segment definitions or aggregates. <br>
Risk: Saved segment plans could accidentally expose raw emails, phone numbers, or customer rows. <br>
Mitigation: Confirm outputs do not echo raw PII and store hashed, aggregated, or named-segment descriptions instead. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/audience-segment-builder) <br>
- [Project homepage from ClawHub metadata](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown segment plan and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should contain segment definitions, aggregate descriptions, suppression rules, and handoff notes rather than raw PII rows.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
