## Description: <br>
Ghost.io Admin API CLI for managing blog posts, pages, tags, and content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visionik](https://clawhub.ai/user/visionik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, site operators, and agents use Ecto to manage Ghost blog content from the command line, including posts, pages, tags, image uploads, webhooks, and site queries. It supports multi-site configuration, markdown-to-HTML content workflows, and JSON output for scripting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Ghost Admin API key grants site-management authority and can be exposed through shared terminals, scripts, logs, screenshots, environment variables, or local configuration files. <br>
Mitigation: Use trusted, pinned releases; keep keys out of shared artifacts; store configuration with restricted permissions; and rotate the Ghost Admin API key if exposure is suspected. <br>
Risk: The CLI can publish, delete, schedule, bulk-change content, upload images, and create or delete webhooks on a configured Ghost site. <br>
Mitigation: Require explicit approval for content-changing actions, confirm the target site before execution, and prefer draft or staging-site workflows before publishing to production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/visionik/skills/ecto) <br>
- [Ghost Admin API](https://ghost.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, json, markdown] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read markdown or stdin content and may produce machine-readable JSON for scripting when commands use --json.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and CHANGELOG, released 2026-01-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
