## Description: <br>
Discovers renewal and replacement opportunities by scanning proposed projects, procurement intentions, and contracts expiring within a 0-180 day window, then ranks the results into an opportunity report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, business development, and capture teams use this skill to find public procurement opportunities where existing contracts are nearing expiration, planned purchases are emerging, or proposed projects create early engagement windows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store credentials locally and may create a free-trial account through device-derived registration when no API key is configured. <br>
Mitigation: Prefer supplying ZLBX_API_KEY through the environment; if using the free-trial flow, review the consent prompt and understand that platform, CPU architecture, and a hashed MAC-derived value are used before an API key is stored in ~/.zlbx/config.json. <br>
Risk: Generated opportunity reports may preserve login-bypass links returned by the API. <br>
Mitigation: Treat generated HTML reports and any sk-bearing links as sensitive, and avoid broad sharing unless granting access through those links is acceptable. <br>
Risk: API scans consume account credits and may send business search terms to the third-party service. <br>
Mitigation: Confirm the intended scan scope and expected credit use before running a scan, and avoid submitting sensitive internal strategy terms as search keywords. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder) <br>
- [Publisher Profile](https://clawhub.ai/user/dragonzu) <br>
- [Workflow Guide](references/workflow.md) <br>
- [API Quick Reference](references/api-quick.md) <br>
- [Report Template](references/report-template.md) <br>
- [Auto-registration Flow](references/auto-register.md) <br>
- [HTML Report Renderer](scripts/render_report.py) <br>
- [ZhiLiao Opportunity Platform](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown opportunity list with an optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes ranked opportunities, source links, data notes, cost estimates, and an absolute path for generated HTML reports.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
