## Description: <br>
Produces a standardized developer handoff package from project design work, including a BRD-style product overview, SRS-style requirements, DD-style technical design, interface source code, and a reference guide. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[encryptshawn](https://clawhub.ai/user/encryptshawn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, PMs, and project stakeholders use this skill to convert project discussions, artifacts, interface code, and partial requirements into a traceable build-documentation package for developer handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads project materials supplied or authorized by the user, which may include sensitive discussions, requirements, or interface source. <br>
Mitigation: Provide only approved project materials and review the generated package before sharing it outside the intended team. <br>
Risk: Generated documentation may preserve unresolved scope, design, or imported-requirement discrepancies as open questions rather than settled facts. <br>
Mitigation: Review the Open Questions and reconciliation notes before treating the package as an implementation contract. <br>
Risk: The workflow writes generated markdown files, copied source files, and a zip archive to disk. <br>
Mitigation: Run it in the intended workspace and inspect output paths and archive contents before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/encryptshawn/skills/build-docs-creator) <br>
- [Product overview reference](references/product-overview.md) <br>
- [Requirements reference](references/requirements.md) <br>
- [Design reference](references/design.md) <br>
- [Interfaces reference](references/interfaces.md) <br>
- [Traceability reference](references/traceability.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documents, copied interface source files, manifest, and zip archive] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a standardized build-docs folder and zip archive; screenshots and rendered images are out of scope.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
