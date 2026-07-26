## Description: <br>
Generate or update an offline IMDF indoor venue map with sensor placement, zone groups, and optional camera analytics overlays. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haixiandaxia-jpg](https://clawhub.ai/user/haixiandaxia-jpg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and venue operations teams use this skill to turn Apple IMDF venue data and optional camera analytics into an offline, single-file interactive indoor map for placement planning, zone grouping, and local review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML can include venue camera analytics that may be sensitive if shared outside the intended audience. <br>
Mitigation: Use lawful, consented, minimized analytics data and share generated HTML only with recipients authorized to view the embedded data. <br>
Risk: Imported placement or group JSON and browser localStorage state can mix data across venue projects. <br>
Mitigation: Review imported JSON before use and set a unique localStorage key for each venue or deployment. <br>
Risk: Schema mismatches in IMDF or analytics columns can produce incomplete maps or misleading analytics totals. <br>
Mitigation: Inspect source file fields, adjust column mappings when needed, and validate the generated map and dashboard data before relying on results. <br>


## Reference(s): <br>
- [Smart Venue Map ClawHub page](https://clawhub.ai/haixiandaxia-jpg/skills/smart-venue-map) <br>
- [HTML map template](artifact/references/html_template.html) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python code, JSON outputs, and a generated single-file HTML map] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes IMDF zip files and optional analytics data locally; generated HTML can embed map and analytics data for offline use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
