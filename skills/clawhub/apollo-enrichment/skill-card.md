## Description: <br>
Apollo.io contact and company enrichment API for enriching people with email, phone, title, and company data; enriching organizations with industry, revenue, employee count, and funding data; and searching for prospects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and go-to-market operators use this skill to enrich contacts and companies through Apollo.io, run bulk contact matching, and search for leads by title, company, location, or keywords. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contact, company, and bulk input data is sent to Apollo.io for lookup and enrichment. <br>
Mitigation: Submit only records, domains, and files that you are allowed to process through Apollo.io. <br>
Risk: The --reveal-email and --reveal-phone options may expose personal contact information. <br>
Mitigation: Use reveal options deliberately and handle returned personal data according to applicable privacy, consent, and retention requirements. <br>
Risk: Apollo enrichment and search requests can consume Apollo credits. <br>
Mitigation: Check Apollo credit usage before large searches or bulk enrichment and limit batch inputs when needed. <br>
Risk: The skill requires delegating an Apollo API key through the APOLLO_API_KEY environment variable. <br>
Mitigation: Use an Apollo API key scoped and managed appropriately for this workflow, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Apollo.io](https://apollo.io) <br>
- [Apollo API Settings](https://app.apollo.io/#/settings/integrations/api) <br>
- [Apollo Credits](https://app.apollo.io/#/settings/credits) <br>
- [ClawHub Skill Page](https://clawhub.ai/capt-marbles/skills/apollo-enrichment) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text or JSON returned by a Python CLI, with setup and usage guidance in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires APOLLO_API_KEY and can consume Apollo credits when enrichment or search commands are run.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
