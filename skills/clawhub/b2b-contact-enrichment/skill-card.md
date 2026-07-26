## Description: <br>
Finds verified professional email addresses with the FinalScout API by LinkedIn profile URL, full name plus company domain, or news article URL, with single and bulk lookup workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davis-lee](https://clawhub.ai/user/davis-lee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, recruiting, marketing, and operations teams use this skill to enrich prospect or author records with verified email addresses through FinalScout. It supports single lookups and bulk batches from LinkedIn URLs, names plus domains, article URLs, CSVs, tables, or JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contact lookups, bulk CSVs, CRM metadata, article URLs, and LinkedIn URLs can share personal or business data with FinalScout. <br>
Mitigation: Use the skill only when authorized to submit the relevant data, and avoid sending unnecessary personal data or sensitive CRM identifiers. <br>
Risk: Bulk CSV export links are public to anyone who has the generated URL until they expire. <br>
Mitigation: Share export links only with intended recipients, retrieve results promptly, and prefer inline summaries when a downloadable file is not needed. <br>
Risk: Webhook URLs and optional personal or generic email lookup settings can broaden data disclosure beyond the local session. <br>
Mitigation: Use trusted webhook endpoints, enable personal or generic email fallback only when appropriate, and review webhook payload handling before bulk runs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davis-lee/skills/b2b-contact-enrichment) <br>
- [FinalScout](https://finalscout.com) <br>
- [FinalScout API settings](https://finalscout.com/app/api/settings) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables, concise summaries, and curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May report task IDs, credit usage, rate-limit details, webhook guidance, and public CSV export links when requested.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
