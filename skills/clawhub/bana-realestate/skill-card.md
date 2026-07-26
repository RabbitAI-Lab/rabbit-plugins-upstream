## Description: <br>
查询巴娜房地产信息 API，覆盖支持城市、小区、二手房、租房和新房。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongweixp](https://clawhub.ai/user/xiongweixp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to query real-estate data for Chinese cities, including communities, second-hand homes, rentals, and new properties. It also helps select API methods, validate request parameters, handle paid-call notices, and interpret returned data without inventing missing fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill collects a Bana AppID and SecureKey for a paid API account. <br>
Mitigation: Treat the SecureKey as a paid-account secret and provide credentials only when the deployment environment and operator are trusted. <br>
Risk: Credentials are saved by default and may also be supplied through command-line arguments. <br>
Mitigation: Prefer one-time use with no saving when possible, avoid exposing credentials in command history or logs, and review local credential-file handling before deployment. <br>
Risk: The API endpoint can be changed with BANA_REALESTATE_BASE_URL. <br>
Mitigation: Use the default endpoint unless a fully trusted test or production destination has been explicitly provided. <br>
Risk: Successful paid methods charge 0.4 yuan per call after fee notice. <br>
Mitigation: Review planned method calls, page counts, and retries before execution, especially for batch requests or upstream failures. <br>


## Reference(s): <br>
- [巴娜房地产信息 API 参考](artifact/references/api.md) <br>
- [巴娜 Skill 技能中心](https://wxpub.aibana.art) <br>
- [ClawHub Skill Page](https://clawhub.ai/xiongweixp/skills/bana-realestate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with JSON API results and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include paid-call fee notices, city/filter/page context, credential handling guidance, and API error explanations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
