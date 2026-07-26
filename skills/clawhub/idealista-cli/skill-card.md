## Description: <br>
Use the idealista CLI to search Idealista listings by location (city, town, area, street) and fetch listing details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjtf93](https://clawhub.ai/user/pjtf93) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to produce Idealista CLI commands for location suggestions, listing searches, listing detail lookups, filtering, and JSON output for scripting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on an idealista CLI executable already installed on PATH, so an untrusted or unexpected local binary could be invoked. <br>
Mitigation: Install idealista-cli only from a trusted source and confirm the executable before using the skill. <br>
Risk: Searches and listing lookups contact Idealista and may expose housing-search details or IDEALISTA_* credential values through prompts, logs, or shared output. <br>
Mitigation: Keep IDEALISTA_* values out of prompts, logs, and shared output, and avoid sharing sensitive housing-search details. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with CLI command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced CLI can return table or JSON output and may require IDEALISTA_* environment variables plus network access to Idealista.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
