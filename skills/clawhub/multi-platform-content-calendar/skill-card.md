## Description: <br>
This skill plans multi-platform content calendars, links schedules to holidays and events, tracks engagement, and generates weekly or monthly planning and review reports for Douyin, Xiaohongshu, Bilibili, and WeChat Official Accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nh5gntnf78-oss](https://clawhub.ai/user/nh5gntnf78-oss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, social media operators, and marketing teams use this skill to plan posts across supported platforms, record performance metrics, and produce weekly plans or monthly review reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local planning files and performance records may contain sensitive campaign details or business metrics. <br>
Mitigation: Use non-sensitive planning data first, review files created under ~/content-calendar, and confirm storage expectations before adding confidential information. <br>
Risk: Calendar recommendations may be unsuitable if fixed holiday data, platform peak times, or entered performance metrics are stale or incorrect. <br>
Mitigation: Review holidays, publication times, goals, and generated reports before using them for public campaigns. <br>
Risk: Optional holiday lookups or performance workflows could expose business details outside the local environment if configured to use external services. <br>
Mitigation: Confirm network behavior and API configuration before enabling external holiday or analytics integrations. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/nh5gntnf78-oss/skills/multi-platform-content-calendar) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports and JSON records, with console text and example shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local content calendar files under ~/content-calendar when the script actions are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
