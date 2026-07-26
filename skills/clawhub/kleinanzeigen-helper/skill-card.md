## Description: <br>
Manage Kleinanzeigen listings through the KleinClaw OpenClaw plugin and embedded miniclaw runtime. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilyazar](https://clawhub.ai/user/ilyazar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare, verify, publish, update, delete, download, and extend Kleinanzeigen listings through the KleinClaw plugin while keeping live account changes scoped and confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The separate KleinClaw plugin can perform live Kleinanzeigen account actions, including publishing, updating, deleting, downloading, and extending listings. <br>
Mitigation: Install only if the KleinClaw plugin is trusted, review the exact listing scope, and require explicit confirmation before any mutating operation. <br>
Risk: Credentials, cookies, browser profiles, session data, or full configuration files could expose sensitive account access details if shared in chat. <br>
Mitigation: Keep those materials out of chat and report only sanitized status, settings, and results. <br>
Risk: Overly broad ad roots or selectors can affect unintended listings. <br>
Mitigation: Keep ad roots narrow, discover matching listings first, and prefer scoped ad handles or explicit ad IDs for live actions. <br>


## Reference(s): <br>
- [KleinClaw plugin](https://clawhub.ai/plugins/kleinclaw) <br>
- [Kleinanzeigen helper skill page](https://clawhub.ai/ilyazar/skills/kleinanzeigen-helper) <br>
- [Prerequisites / Install](references/install.md) <br>
- [Non-negotiables](references/non-negotiables.md) <br>
- [Workflow](references/workflow.md) <br>
- [Ad Authoring](references/ad-authoring.md) <br>
- [Draft Publish Preflight](references/draft-publish-preflight.md) <br>
- [Listing Discovery and Scoping](references/listing-discovery-scoping.md) <br>
- [Browser Behaviour](references/browser-behaviour.md) <br>
- [Publish Result Caveats](references/publish-result-caveats.md) <br>
- [Tool Selection](references/tool-selection.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration instructions, Shell commands] <br>
**Output Format:** [Markdown guidance with inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should stay sanitized and should not include credentials, cookies, browser profiles, session data, or full configuration files.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
