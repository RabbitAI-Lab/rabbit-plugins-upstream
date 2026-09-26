## Description:

Watches websites and reports what broke: uptime checks that alert when a site goes down and again when it recovers, Vercel error logs and Core Web Vitals, and GA4 traffic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and operations teams use this skill to check whether configured websites are up, set up scheduled outage alerts, and route Vercel or GA4 questions to the matching installed skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and applying the schedule can create recurring monitoring jobs and local alert state.

Mitigation: Review the generated schedule and configuration before running schedule --apply, and confirm the desired notification target.

Risk: When Vercel or GA4 modules are enabled, the skill reads delegated skill credentials from OpenClaw config and passes them to the matching child skill.

Mitigation: Enable only the modules needed, keep credentials in OpenClaw configuration, and verify delegated skills are trusted and configured for the intended project or property.

Risk: Raw Vercel log messages may contain application secrets or customer data if explicitly enabled.

Mitigation: Keep includeMessages disabled unless operators have reviewed the log content and approved delivery into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anatoli-iliev/skills/web-observer)
- [Project homepage](https://github.com/anatoli-iliev/web-observer)
- [OpenClaw Vercel Insights dependency](https://github.com/anatoli-iliev/openclaw-vercel-insights)
- [Open GA4 dependency](https://github.com/anatoli-iliev/open-ga4)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command output summaries; some commands can emit JSON or tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on configured watches and on whether the delegated Vercel and GA4 skills are installed and configured.]

## Skill Version(s):

0.1.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
