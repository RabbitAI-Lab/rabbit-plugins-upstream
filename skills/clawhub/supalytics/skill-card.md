## Description: <br>
Query web analytics data using the Supalytics CLI for pageviews, visitors, top pages, traffic sources, revenue metrics, conversions, funnels, events, and realtime visitors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yogesharc](https://clawhub.ai/user/yogesharc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, site owners, and analytics operators use this skill to install and run Supalytics CLI commands for web analytics reporting, realtime traffic checks, event analysis, revenue attribution, and site configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup guidance includes administrator-level symlink commands for system paths. <br>
Mitigation: Prefer adding ~/.bun/bin to PATH; review any sudo symlink command before running it. <br>
Risk: Supalytics CLI commands can access analytics account data and site configuration. <br>
Mitigation: Install only if you trust Supalytics, authenticate intentionally, and run site add, update, remove, or default commands only when you mean to change analytics configuration. <br>


## Reference(s): <br>
- [Supalytics homepage](https://supalytics.co) <br>
- [Bun runtime](https://bun.sh) <br>
- [ClawHub skill page](https://clawhub.ai/yogesharc/skills/supalytics) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Supalytics CLI and Bun runtime; OAuth login may require browser interaction.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
