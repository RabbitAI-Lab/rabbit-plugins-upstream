## Description: <br>
Query and sync YApi interface documentation for request and response details, YApi URLs, and documentation synchronization workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and API documentation maintainers use this skill to query YApi interface definitions, summarize methods, paths, headers, parameters, request bodies, and response schemas, and synchronize documentation through the configured YApi CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask the agent to use a configured YApi CLI or fallback npm package against a sensitive YApi instance. <br>
Mitigation: Install only when intentional, review the npm package source and token scope for sensitive instances, and confirm authentication with the intended account. <br>
Risk: Documentation sync can write local .yapi files and update generated documentation mappings. <br>
Mitigation: Run docs-sync with --dry-run first and inspect generated .yapi changes before committing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leeguooooo/skills/yapi) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose YApi CLI commands, summarize fetched interface JSON, and identify files changed by docs-sync workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
