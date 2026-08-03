## Description: <br>
Data Analysis Toolkit helps agents clean data, run statistical analysis, recommend visualizations, and generate Python analysis code for business, research, reporting, and exploratory analysis workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and research users use this skill to turn text, JSON, or CSV inputs into data-cleaning guidance, statistical summaries, visualization recommendations, and executable Python snippets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may write files and run commands through the hosting agent, which can affect the local workspace if used without review. <br>
Mitigation: Run it in a scoped workspace or sandbox, review proposed commands and file writes before approval, and grant only the permissions needed for the current analysis. <br>
Risk: The skill can process datasets and includes optional callback behavior, creating a data-exposure risk for sensitive inputs. <br>
Mitigation: Avoid sensitive datasets unless external API and callback behavior are disabled or explicitly approved, and redact private fields before analysis. <br>
Risk: Generated analysis, statistical conclusions, or visualization code can be misleading when input data is incomplete, biased, or malformed. <br>
Mitigation: Validate inputs, inspect assumptions and generated code, and verify statistical results before using them for business or research decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-style structured responses with Python code blocks and execution logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write files, run commands, and optionally use callback URLs when the hosting agent allows those actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
