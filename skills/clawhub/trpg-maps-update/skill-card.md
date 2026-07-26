## Description: <br>
Updates existing TRPG briefing_package map systems by moving large structured maps into maps/, replacing large scene initial_map blocks with map_ref, and adding optional map_config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators maintaining TRPG briefing_package projects use this skill to reorganize large structured map YAML, update scene map references, and configure a visual map panel when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Moving and deleting map YAML can remove custom map data if files are incomplete or misidentified. <br>
Mitigation: Keep a backup or version control checkpoint, confirm moved map YAML is complete, and delete the old data/ copy only after verifying the maps/ copy. <br>
Risk: Updated scene map_ref values can break map loading if paths or map names do not match the moved files. <br>
Mitigation: Check each scene reference against the maps/ directory and test the briefing_package map panel after the update. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/ice26985850/skills/trpg-maps-update) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code] <br>
**Output Format:** [Markdown guidance with YAML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in briefing_package file edits for map YAML, scene YAML, and config.yaml.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
