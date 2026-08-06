## Description: <br>
Provides JFTech device cloud-storage video listing, playback/download URL retrieval, and cloud alarm message queries for devices with an active cloud-storage plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query JFTech cloud camera recordings, obtain playback or download URLs, and review cloud alarm messages after configuring the required JFTech credentials and device identifiers. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive camera recordings and can print playback or download URLs to the console. <br>
Mitigation: Run it only in trusted terminals and avoid command histories, logs, shared screens, or transcripts that could expose video URLs. <br>
Risk: JF_APP_SECRET and JF_DEVICE_TOKEN are sensitive credentials required for API access. <br>
Mitigation: Store credentials in a secure environment manager, limit access to the runtime environment, and rotate credentials if exposure is suspected. <br>
Risk: JF_ENDPOINT can be overridden, which could send signed requests to an untrusted host. <br>
Mitigation: Set JF_ENDPOINT only to trusted JFTech regional hosts such as the documented CN, AS, EU, or NA endpoints. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-cloud-record) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jftech) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and console text or JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print sensitive playback or download URLs that are valid for 24 hours.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact metadata reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
