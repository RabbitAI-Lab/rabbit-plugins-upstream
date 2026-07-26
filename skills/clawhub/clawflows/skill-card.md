## Description: <br>
Searches, installs, and runs multi-skill automations from clawflows.com, combining multiple skills into workflows with logic, conditions, and data flow between steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cluka-399](https://clawhub.ai/user/cluka-399) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use Clawflows to discover, install, check, run, and publish workflow automations that coordinate multiple agent skills through capability-based steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install and run external workflows that may use other skills to change data, send messages, access accounts, publish content, or run on a schedule. <br>
Mitigation: Inspect downloaded workflow YAML, run `clawflows check`, use `--dry-run`, and review sensitive actions before execution. <br>
Risk: Use depends on trusting the `clawflows` npm CLI and the automations selected from its registry. <br>
Mitigation: Install only after reviewing the CLI/package source and choose workflows whose requested capabilities match the intended task. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cluka-399/skills/clawflows) <br>
- [ClawFlows Registry](https://clawflows.com) <br>
- [Clawflows npm Package](https://www.npmjs.com/package/clawflows) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and YAML code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation or download of automation YAML files when the CLI commands are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
