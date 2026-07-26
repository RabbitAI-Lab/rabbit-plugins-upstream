## Description: <br>
This skill helps agents call LinkFox-routed Temu Global Ads APIs for creating, modifying, checking, and reporting on search and recommendation ads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu sellers, operators, and developers use this skill to run or script global advertising workflows through LinkFox, including ad creation, budget and ROAS changes, detail queries, operation logs, and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses LinkFox and Temu credentials and can store Temu access tokens locally. <br>
Mitigation: Use dedicated least-privilege credentials where available, restrict token-store file access, avoid sharing saved token files, and rotate tokens after shared or elevated use. <br>
Risk: Generic Temu proxy and file-download scripts may provide broader account access than Ads-only workflows. <br>
Mitigation: Limit calls to the documented Ads endpoints, review the requested type and parameters before execution, and avoid using generic proxy behavior for unrelated account operations. <br>
Risk: Ad modification calls can delete, pause, reopen, or change budget and ROAS settings. <br>
Mitigation: Manually confirm target goods IDs, status values, budget values, and ROAS values before running modification commands. <br>
Risk: Full API responses are persisted locally and may contain business or account data. <br>
Mitigation: Review the local linkfox output directory, avoid inline output for sensitive payloads, and remove or protect response logs before sharing the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-global) <br>
- [Temu Partner Global Ads documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>
- [LinkFox Temu Ads API reference](references/api.md) <br>
- [Temu accessToken authorization](references/access-token.md) <br>
- [Partner Global Ads catalog](references/partner-global-catalog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, Python script calls, and JSON API responses saved to local files or printed to stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and Temu access tokens; large responses are summarized on stdout while full responses are persisted under a local linkfox session directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
