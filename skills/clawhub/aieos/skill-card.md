## Description: <br>
AIEOS helps agents load, validate, apply, export, and present portable persona schemas for consistent identity, behavior, and memory across OpenClaw-style environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeglin](https://clawhub.ai/user/zeglin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agent builders, and agent operators use this skill to manage AI persona data with the AIEOS standard, including validating schemas, previewing identity updates, applying persona files, exporting current identity data, and generating a public bio page. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Applying a schema can persistently change agent persona files including entity.json, IDENTITY.md, and SOUL.md. <br>
Mitigation: Run the apply command as a dry run first, inspect the proposed changes, and back up existing identity files before using --apply. <br>
Risk: Schemas can be loaded from URLs or local files, so untrusted schema content could introduce unwanted persona changes. <br>
Mitigation: Use trusted schema sources, review imported JSON before applying it, and avoid schemas from unknown URLs. <br>
Risk: Generated public bio pages may expose persona details or include image URLs from the persona data. <br>
Mitigation: Review generated HTML before publishing or sharing it. <br>


## Reference(s): <br>
- [AIEOS schema file](aieos.schema.json) <br>
- [Official AIEOS schema](https://aieos.org/schema/v1/aieos.schema.json) <br>
- [ClawHub skill page](https://clawhub.ai/zeglin/skills/aieos) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; JSON persona data; Markdown identity files; generated HTML output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Dry-run output is shown by default for apply operations; file writes require explicit --apply or an output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
