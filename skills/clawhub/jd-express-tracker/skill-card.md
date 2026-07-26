## Description: <br>
JD Express Tracker helps agents track JD Logistics waybills, estimate delivery timing, diagnose delays, and summarize multiple shipments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xuhui-xiaohe](https://clawhub.ai/user/xuhui-xiaohe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and support agents use this skill to check JD Logistics package status, review tracking timelines, estimate delivery windows, and get next-step guidance for delayed or abnormal shipments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Waybill numbers and JD session tokens can expose shipment or account information if they are logged, hard-coded, or shared unnecessarily. <br>
Mitigation: Use the skill only for shipments the user is authorized to check, provide JD session tokens through secure secret handling, avoid logging tokens or full waybill data, and account for the local recent-history cache. <br>
Risk: Tracking results may be delayed or incomplete because JD Logistics data can lag and non-JD waybills are not supported. <br>
Mitigation: State that tracking data is for reference, validate JD waybill prefixes before querying, and direct users to the JD app for account-bound actions such as courier contact or delivery changes. <br>


## Reference(s): <br>
- [JD Express waybill API specification](skills/jd-express-tracking/references/api-spec.md) <br>
- [ClawHub skill page](https://clawhub.ai/xuhui-xiaohe/skills/jd-express-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown tracking summaries with status cards, timelines, ETA notes, and exception guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May process up to 10 JD waybills per request and should display sensitive waybill or operator data only in minimized or masked form.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
