## Description: <br>
Generates a Jenkins plugin skeleton from the Jenkins version, JDK version, plugin metadata, and extension point selected by the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leoyim](https://clawhub.ai/user/leoyim) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold Jenkins plugin projects with Maven configuration, Java extension classes, Jelly configuration views, README content, build commands, installation steps, and troubleshooting guidance matched to their Jenkins and JDK versions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate on broad Jenkins plugin development requests and may scaffold a full project when the user only wanted advice or review. <br>
Mitigation: State whether the desired outcome is full scaffolding, design advice, or code review before invoking the skill. <br>
Risk: Incorrect Jenkins or JDK versions can lead to incompatible Maven parent, Java level, or generated plugin behavior. <br>
Mitigation: Provide exact Jenkins and JDK versions and review the generated compatibility summary before building or installing the plugin. <br>
Risk: Generated plugin code and configuration may need project-specific review before use in a Jenkins controller. <br>
Mitigation: Review generated Java, Jelly, Maven configuration, and README content, then build and test locally with `mvn hpi:run` before deploying. <br>


## Reference(s): <br>
- [Jenkins Plugin Developer Documentation](https://www.jenkins.io/doc/developer/) <br>
- [Jenkins Java Support Policy](https://www.jenkins.io/doc/book/platform-information/support-policy-java/index.html) <br>
- [Jenkins Plugin POM](https://github.com/jenkinsci/plugin-pom) <br>
- [Jenkins Hello World Plugin](https://github.com/jenkinsci/hello-world-plugin/) <br>
- [Jenkins Public Maven Repository](https://repo.jenkins-ci.org/public/) <br>
- [Plugin Types Reference](references/plugin-types.md) <br>
- [Trigger Timing Reference](references/trigger-timing-reference.md) <br>
- [Compatibility Check](references/compatibility-check.md) <br>
- [Jelly Reference](references/jelly-reference.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with code blocks, file trees, Maven XML, Java source, Jelly XML, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks for missing Jenkins, JDK, plugin metadata, extension point, feature toggles, and output language before generating files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
