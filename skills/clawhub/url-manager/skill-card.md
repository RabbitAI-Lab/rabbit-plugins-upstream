## Description: <br>
url-manager helps agents save, organize, search, and share web links and notes in hosted URL Manager collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[piccolo123](https://clawhub.ai/user/piccolo123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill through an agent to collect URLs or notes, organize them into categories and shared collections, search saved content, and deliver results through a card-based web interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and store account credentials for ai.ocean94.com and keep a bearer token in the skill directory. <br>
Mitigation: Install only after confirming the user accepts an agent-managed account and local token storage. <br>
Risk: Saved URLs and notes are stored on the hosted ai.ocean94.com service. <br>
Mitigation: Inform the user before first use and avoid saving private links or notes unless the user explicitly agrees. <br>
Risk: Generated magic links or invite links may grant access to account content or shared collections. <br>
Mitigation: Treat generated links as account-access or sharing links and share them only with intended recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/piccolo123/skills/url-manager) <br>
- [URL Manager service](https://ai.ocean94.com/) <br>
- [User Agreement](https://ai.ocean94.com/terms.html) <br>
- [Privacy Policy](https://ai.ocean94.com/privacy.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with command examples and generated links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate hosted magic links, invite links, and JSON output when commands are run with --json.] <br>

## Skill Version(s): <br>
2.6.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
