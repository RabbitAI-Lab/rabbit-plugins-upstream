## Description: <br>
Prospector finds B2B leads matching an ICP by searching companies with Exa, enriching contacts with Apollo, exporting CSV results, and optionally syncing to Attio CRM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[slempiam](https://clawhub.ai/user/slempiam) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, sales operators, and go-to-market teams use Prospector to collect ICP criteria, search for matching companies, enrich decision-maker contacts, and export or sync lead lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys for Exa, Apollo, and Attio may grant access to vendor accounts if exposed. <br>
Mitigation: Use revocable, least-privilege API keys, prefer environment variables where practical, keep local config permissions owner-only, and rotate keys when the skill is no longer used. <br>
Risk: Search criteria and contact data may be processed by Exa, Apollo, and Attio. <br>
Mitigation: Use the skill only with data the user is authorized to process and review vendor handling requirements before sending or syncing lead data. <br>
Risk: Exported Desktop CSV files contain plaintext personal or business contact data and may be synced or backed up by the operating system. <br>
Mitigation: Store, share, and delete CSV exports according to the user's data retention and privacy requirements. <br>


## Reference(s): <br>
- [Prospector ClawHub Skill Page](https://clawhub.ai/slempiam/skills/prospector) <br>
- [Exa](https://exa.ai) <br>
- [Apollo](https://apollo.io) <br>
- [Attio](https://attio.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, API calls] <br>
**Output Format:** [Markdown guidance with bash and Python command blocks, plus CSV lead exports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Exports lead data to a Desktop CSV file and can optionally sync companies and contacts to Attio when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
