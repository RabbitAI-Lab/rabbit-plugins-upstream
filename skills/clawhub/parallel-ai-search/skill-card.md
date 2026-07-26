## Description: <br>
Use Parallel's parallel-cli to do live web search, URL extraction, deep research reports, bulk data enrichment, entity discovery, and web monitoring with cited results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route current-information tasks to Parallel CLI commands for search, extraction, deep research, structured enrichment, entity discovery, and ongoing web monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install Parallel CLI through a remote shell installer and allows broad curl usage. <br>
Mitigation: Prefer the pipx install path or inspect and verify the install script before running it. <br>
Risk: Parallel CLI authentication uses an API key or login session that could be exposed through chat, shell history, or shared environments. <br>
Mitigation: Use a dedicated Parallel API key and avoid pasting secrets into chat or commands that persist in shell history. <br>
Risk: Monitor mode can create recurring web tracking and optionally send events to a webhook. <br>
Mitigation: Confirm monitor cadence and webhook destination before enabling ongoing tracking. <br>


## Reference(s): <br>
- [Parallel CLI documentation](https://docs.parallel.ai/integrations/cli) <br>
- [Command templates](references/command-templates.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/parallel-ai-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON, CSV, or markdown file paths from Parallel CLI outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May cite web sources, save long outputs under /tmp, and report async run or monitor identifiers when Parallel CLI jobs continue server-side.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
