## Description: <br>
JF Open Pro AI Outdoor helps agents manage JF outdoor security monitoring functions, including vehicle detection, abnormal alarms, smart detection, sensitivity settings, detection areas, and push schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, installers, and operations teams use this skill to administer JF outdoor security devices through scripted API actions for monitoring, alarms, vehicle records, detection settings, notification plans, statistics, and device credential sync. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America, based on the documented JF API regions in the artifact. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make lasting security and device-management changes, including disabling services, changing detection settings, deleting schedules or vehicles, and syncing device credentials. <br>
Mitigation: Require explicit confirmation before delete, disable, credential-sync, or configuration-change actions; prefer read-only query actions first to verify the target device and account. <br>
Risk: The skill handles sensitive JF app secrets, JWT authorization tokens, device serial numbers, and device login credentials. <br>
Mitigation: Use a dedicated administrative account, keep credentials in protected environment variables or a secret manager, avoid logging secrets, and rotate credentials after testing or suspected exposure. <br>
Risk: The scripts send authenticated POST requests to JF regional API endpoints that may affect real outdoor security devices. <br>
Mitigation: Verify the region endpoint, device serial number, user identifier, and action parameters before execution, especially in production monitoring environments. <br>


## Reference(s): <br>
- [JF Developer Platform](https://developer.jftech.com) <br>
- [JF Signature Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=609261d9bb5049c3a2fc7222adf465fb&lang=zh) <br>
- [JF Timestamp Algorithm Documentation](https://docs.jftech.com/docs?menusId=2531aba7e2d84e13ad8ce977007922f3&siderId=8da7ad6119fd41159e2026c71ddb3555&lang=zh) <br>
- [JF Outdoor Security API Documentation](https://docs.jftech.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JF account, app, device, authorization, and region configuration before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact metadata.version is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
