## Description:

JF Open Algo Assistant helps agents guide users through JFTech Open Platform AI detection workflows, recommend supported no-database algorithms, call image or camera analysis APIs, and produce structured detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jftech](https://clawhub.ai/user/jftech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to select JFTech Open Platform detection algorithms for safety, retail, perimeter, vehicle, environmental, and camera-image analysis scenarios. The skill can configure credentials, open selected algorithms, call synchronous analysis APIs, and summarize detections with optional annotated evidence images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send target images, camera identifiers, and analysis results to a third-party API.

Mitigation: Install and run it only when the operator trusts JFTech and is authorized to process the relevant imagery and device data.

Risk: The skill stores API credentials in a local config.json file.

Mitigation: Protect the skill directory, avoid sharing config.json, and rotate credentials if the file may have been exposed.

Risk: The optional camera-capture path can install a dependent skill from an unpinned remote source.

Mitigation: Review and pin the jf-open-pro-capture dependency before using automatic installation.

Risk: Detection results may be incomplete or sensitive, especially for surveillance and workplace monitoring use cases.

Mitigation: Review outputs before acting on them, tune confidence thresholds with domain context, and avoid sensitive or regulated imagery without consent and lawful basis.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [JFTech Open Platform algorithm reference](artifact/reference.md)
- [Algorithm metadata](artifact/algorithms.json)
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-algo-assistant)
- [JFTech Open Platform API endpoint](https://api.jftechws.com)
- [Dependent camera capture skill](https://clawhub.ai/jftech/jf-open-pro-capture)
- [Dependent camera capture source](https://gitee.com/jftek/jftech-open-skills/tree/main/jf-open-pro-capture)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown, files]

**Output Format:** [Markdown guidance with shell commands, JSON API results, and optional generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local config.json, result JSON files, and annotated evidence images when run with user-provided credentials and images.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
