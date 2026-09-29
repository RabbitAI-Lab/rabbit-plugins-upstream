## Description:

Helps agents provision, access, inspect, and terminate standalone UCloud AstraFlow desktop sandboxes with browser-based remote desktops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lijinhongucl-pixel](https://clawhub.ai/user/lijinhongucl-pixel)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and other users can create regional remote Linux desktops for browser-based testing, inspect active sandboxes, connect through noVNC, and terminate them when finished.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A supplied target URL can break into shell commands.

Mitigation: Do not pass untrusted or user-supplied URLs to --url until URL handling is safely quoted or otherwise fixed.

Risk: The noVNC access URL contains the VNC password.

Mitigation: Treat the URL as a secret; do not publish it in logs, messages, or shared documents.

Risk: The skill requires an AstraFlow API key and can create billable desktops.

Mitigation: Protect the API key, confirm the lifespan before creation, and terminate unused sandboxes promptly.

## Reference(s):

- [AstraFlow Remote Lab release](https://clawhub.ai/lijinhongucl-pixel/skills/astraflow-remote-lab)
- [AstraFlow API reference](references/api_reference.md)
- [AstraFlow API key management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and sandbox connection details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a sandbox ID, region, timezone, and a sensitive noVNC access URL.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
