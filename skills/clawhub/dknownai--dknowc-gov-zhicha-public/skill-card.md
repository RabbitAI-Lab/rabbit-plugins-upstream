## Description: <br>
ClawHub Public release of DKnowC Gov Zhicha helps agents answer government-service, public-service, social-security, housing-fund, certification, subsidy, policy-eligibility, process, materials, entry-point, and official-basis questions using DKnowC trusted unified government information sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dknownai](https://clawhub.ai/user/dknownai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer China government affairs and public-service questions with actionable steps, required conditions, materials, channels, and cited official basis. It can also return public-service item lists, policy-file lists, and structured JSON for downstream tooling. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Setup handles a phone number, SMS verification code, and a generated local API key. <br>
Mitigation: Collect the phone number and code only for setup, do not display or republish the API key, and treat config.ini as sensitive local-only configuration. <br>
Risk: Registration or chat requests can be redirected with custom --base or --endpoint values. <br>
Mitigation: Use the default official DKnowC endpoints unless the override target is fully trusted and reviewed. <br>
Risk: Sharing an installed skill directory can expose the generated config.ini. <br>
Mitigation: Remove config.ini before sharing, packaging, or publishing any installed copy of the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknowc-gov-zhicha-public) <br>
- [DKnowC trusted unified interface endpoint](https://open.dknowc.cn/chat/trusted/unification) <br>
- [DKnowC platform registration](https://platform.dknowc.cn/auth/#/register?channel=2787E171-B0E5-4328-9946-47AC52434D1F&type=11) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown answer with source fields; optional structured JSON via --json-only; setup uses shell commands and local config.ini.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers may include reference materials, public-service items, policy files, safety status, knowledge scope, region, and source URLs. Setup may create a local config.ini containing a sensitive API key.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata, artifact _meta.json, changelog released 2026-07-14) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
