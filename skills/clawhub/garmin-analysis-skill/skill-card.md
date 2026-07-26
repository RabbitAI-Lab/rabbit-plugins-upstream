## Description: <br>
Provides structured workflows for using the cycling-health CLI to sync Garmin China Wellness data to Intervals.icu, analyze Garmin, Intervals.icu, and iGPSPORT cycling and recovery data, and query Strava and Xingzhe cycling resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baijian](https://clawhub.ai/user/baijian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate the cycling-health CLI for Garmin, Intervals.icu, iGPSPORT, Strava, and Xingzhe cycling and health workflows. It supports health synchronization, ride and recovery analysis, route queries, guarded downloads, and account-specific read or write workflows with preview-first handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides access to sensitive cycling, health, credential, OAuth token, API key, downloaded FIT/GPX, and account metadata. <br>
Mitigation: Install only if comfortable granting the cycling-health CLI access to those accounts, use local authentication or protected files for secrets, and do not paste secrets into chat. <br>
Risk: Some workflows can perform live synchronization, settings changes, event changes, credential revocation, overwrites, or route/file downloads. <br>
Mitigation: Review previews before confirming changes, require explicit authorization for --confirm or --overwrite, and reject destination overwrites unless the user approves them after reviewing the effect. <br>
Risk: The iGPSPORT integration is described as an unsupported private API and may have endpoint, signing, payload, or account-specific failures. <br>
Mitigation: Label iGPSPORT results as coming from an unsupported private iGPSPORT CN integration, preserve exact CLI errors, and avoid merging iGPSPORT records with Garmin or Intervals data unless identity and duplication are established. <br>
Risk: The CLI self-upgrade may update the local executable before analysis or sync commands. <br>
Mitigation: Run the documented upgrade check, report upgrade failures or checksum problems, and continue with the installed binary only when the user has authorized that fallback. <br>
Risk: Cycling and recovery conclusions can be misleading if missing sensor channels, duplicate sources, or short-term recovery data are treated as durable fitness changes. <br>
Mitigation: Analyze only returned fields, state source, date range, region or profile, preserve data gaps, and separate observed values from interpretation and confidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baijian/skills/garmin-analysis-skill) <br>
- [cycling-health public CLI](https://github.com/baijian/cycling-health) <br>
- [Garmin CLI Workflows](references/cli-workflows.md) <br>
- [Intervals.icu CLI Workflows](references/intervals-workflows.md) <br>
- [iGPSPORT CLI Workflows](references/igpsport-workflows.md) <br>
- [Strava CLI Workflows](references/strava-workflows.md) <br>
- [Xingzhe CLI Workflows](references/xingzhe-workflows.md) <br>
- [Feedback and issues](https://discord.gg/R6xPZc5Dg) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output expectations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emphasizes staged data collection, --output json, profile and region labeling, preview-first writes, and explicit confirmation for destructive or live changes.] <br>

## Skill Version(s): <br>
0.2.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
