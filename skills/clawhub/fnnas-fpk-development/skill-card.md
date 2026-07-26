## Description: <br>
Guides agents through the full FNNAS fnOS FPK application development workflow, including project creation, configuration, building, debugging, testing, and publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songxf1024](https://clawhub.ai/user/songxf1024) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, configure, package, test, and publish FNNAS fnOS FPK applications. It is most useful when an agent needs to produce FPK project guidance, manifests, privilege and resource configuration, lifecycle scripts, shell commands, or release checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: FPK build, install, publish, upload, manual-install, global npm install, and root-permission steps can change a local development machine, NAS device, or published application state. <br>
Mitigation: Use a test NAS where practical, review package provenance and requested permissions, avoid root unless necessary, and keep backups or rollback plans for important data. <br>
Risk: Project-specific guidance can be wrong if the target platform, UI entry mode, or installer-wizard needs are assumed. <br>
Mitigation: Confirm the target platform, UI entry behavior, and installer-wizard requirement before generating concrete FPK configuration or commands. <br>


## Reference(s): <br>
- [Bundled FNNAS Development Documentation](references/ALL_DOCS.md) <br>
- [FNNAS Developer Guide](https://developer.fnnas.com/docs/guide) <br>
- [FNNAS Developer Platform](https://developer.fnnas.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code, shell command blocks, configuration examples, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the bundled FNNAS documentation as the primary reference and asks prerequisite questions before project-specific guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
