## Description: <br>
依托全球蜜罐网络及百万级节点构建的IP情报分析平台，提供精准的IP画像与威胁预警服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security analysts, developers, and operations teams use this skill to query threat intelligence for an IP address, including location, ASN, and historical malicious activity signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the external API key in a local .env file in plaintext. <br>
Mitigation: Prefer an environment variable or secret store, keep .env out of source control and backups, and rotate any key that has already been saved locally. <br>
Risk: The skill writes local configuration when saving the API key. <br>
Mitigation: Review the working directory before use and confirm where .env will be created or updated. <br>
Risk: Unrelated gaokao and school-query references make the skill scope less clear. <br>
Mitigation: Confirm those references are documentation leftovers and that active behavior is limited to IP threat intelligence lookup before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/xby-ip-query) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Configuration guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value before querying the upstream service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
