## Description: <br>
Tasteprint helps an agent build and use a user-owned preference profile for product, shopping, gift, gear, and purchase recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaodushi](https://clawhub.ai/user/zaodushi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Tasteprint to create, update, inspect, sync, delete, and apply a local recommendation profile for user-authorized product recommendations. It is intended for workflows where the user explicitly consents to profile collection or chooses a questionnaire-based profile instead. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to collect and persist sensitive shopping, content, social, and ChatGPT behavior in a local profile. <br>
Mitigation: Use it only with explicit user consent, review the retained profile data, and delete the profile directory when the user no longer wants the data stored. <br>
Risk: The artifact references consent, schema, platform, browser, and analysis files that are not present in the bundle, leaving important controls incomplete. <br>
Mitigation: Verify that the missing reference files or equivalent controls define consent, retained data, review, and deletion behavior before running browser collection. <br>
Risk: Browser collection may require access to signed-in user accounts. <br>
Mitigation: Grant browser access only in a user-owned session and avoid running collection against accounts or platforms that the user has not authorized. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/zaodushi/Tasteprint.skill) <br>
- [ClawHub skill listing](https://clawhub.ai/zaodushi/skills/tasteprint-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-backed profile and collection status files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local Tasteprint profile data under the skill directory when the user authorizes collection or profile management.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
