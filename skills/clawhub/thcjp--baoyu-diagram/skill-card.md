## Description: <br>
Baoyu Diagram helps agents create professional dark-themed SVG diagrams, including architecture diagrams, flowcharts, and sequence-style diagrams, from natural-language requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and automation users use this skill to ask an agent for static SVG diagrams for architecture, process, sequence, UI, report, or data-visualization materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad read/write/command authority could affect files, commands, credentials, or external services if granted without supervision. <br>
Mitigation: Run the skill in a sandboxed agent environment, grant only the tools needed for the specific diagram task, and review proposed file writes or commands before execution. <br>
Risk: Generated diagrams or supporting explanations may be incorrect or misleading when the prompt or source context is incomplete. <br>
Mitigation: Review the generated SVG, labels, flows, and assumptions before publishing or using the result in business or technical decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with SVG/code outputs, JSON examples, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be reviewed before file writes, command execution, API use, or publication.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
