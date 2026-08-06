## Description: <br>
Provides JF Tech elderly-care device commands for checking and changing care service status, configuring abnormal-behavior alerts, and querying fall, routine, and diet data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, and integrators use this skill to operate authorized JF Tech elderly-care monitoring devices, review alerts and activity summaries, and adjust monitoring settings. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America, based on the documented service regions; review routing before use outside China because the scripts use the China API endpoint. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive monitoring data, including credentials, authorization tokens, device identifiers, alarm records, routine data, diet data, and returned media references. <br>
Mitigation: Install and run it only with appropriate consent or lawful caregiver authority, and protect credentials and returned monitoring data as sensitive information. <br>
Risk: Switch and configuration actions can change safety-related elderly-care monitoring settings without an additional built-in confirmation step. <br>
Mitigation: Manually confirm switch and configuration commands before execution, especially when disabling care monitoring or changing abnormal-behavior thresholds. <br>
Risk: The scripts use the China JF Tech API endpoint even though the skill documentation lists multiple service regions. <br>
Mitigation: Review endpoint routing, regional availability, and data-transfer requirements before using the skill outside China. <br>
Risk: Some helper calls reference the move-card signing value without passing it through every query function, which may cause selected API commands to fail until corrected in the runtime environment. <br>
Mitigation: Test each action in a non-production environment and ensure the signing move-card value is correctly supplied before relying on the skill for caregiving workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-ai-elderly-care) <br>
- [JF Tech developer portal](https://developer.jftech.com) <br>
- [JF Tech signature algorithm documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=609261d9bb5049c3a2fc7222adf465fb&lang=zh) <br>
- [JF Tech timestamp algorithm documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=8da7ad6119fd41159e2026c71ddb3555&lang=zh) <br>
- [JF Tech package card usage documentation](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=d2c0d9105d9c4b78bc0d2ee3851d2557&lang=zh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Command-line text or JSON responses from JF Tech API calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires authorized JF Tech credentials, a bound online device, and an active elderly-care package.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
