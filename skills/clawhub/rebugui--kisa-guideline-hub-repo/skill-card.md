## Description: <br>
Automatically collect and publish security guidelines and guides from KISA and Boho to Notion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rebugui](https://clawhub.ai/user/rebugui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to collect KISA and Boho security guideline updates, download associated PDFs, and publish guideline records into a configured Notion database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can repeatedly write guideline records and file attachments to Notion using local credentials. <br>
Mitigation: Use a least-privilege Notion token scoped to the intended database, verify database IDs before publishing, and run collection before publishing when possible. <br>
Risk: The published artifact relies on external local security-news-module code that is not included in the reviewed artifact. <br>
Mitigation: Review the referenced local module before running the skill and avoid enabling recurring schedules until the full local dependency chain has been inspected. <br>
Risk: A shared local .env file may contain unrelated secrets that are available to the publishing workflow. <br>
Mitigation: Inspect the .env file before execution and isolate credentials so only the Notion and database values needed for guideline publishing are present. <br>


## Reference(s): <br>
- [Notion Database Schema for Guidelines](references/schema.md) <br>
- [Example Guideline Publications](references/examples.md) <br>
- [KISA Guidelines Source](https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/2060207) <br>
- [Boho Security Portal](https://www.boho.or.kr) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with bash commands and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can publish records and PDF attachments to Notion when run with configured local credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
