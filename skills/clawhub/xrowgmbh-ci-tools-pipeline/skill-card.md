## Description: <br>
Build and maintain GitLab CI/CD pipelines with the CI Tools Components Catalog at ci-tools.xrow.de. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DevOps engineers use this skill to create, repair, and validate GitLab CI/CD pipelines using CI Tools catalog components for applications, Helm charts, containers, packages, documentation, infrastructure, and GitOps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run remote GitLab actions such as pushing branches or starting merge request pipelines. <br>
Mitigation: Confirm the target branch or merge request, token permissions, and repository policy before approving git push or glab ci run commands. <br>
Risk: The documented workflow includes pushing with CI skipped before starting an MR pipeline. <br>
Mitigation: Verify that skipping push CI is acceptable for the repository and use the narrowest validation path that preserves required checks. <br>


## Reference(s): <br>
- [CI Tools Catalog](https://ci-tools.xrow.de/) <br>
- [CI Tools Components](https://ci-tools.xrow.de/Components/) <br>
- [CI Tools Source](https://gitlab.com/xrow-public/ci-tools) <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitLab CI component selections, .gitlab-ci.yml changes, validation commands, and review guidance.] <br>

## Skill Version(s): <br>
1.78.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
