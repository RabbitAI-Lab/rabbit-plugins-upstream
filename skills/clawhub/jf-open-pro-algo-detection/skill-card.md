## Description:

Guides an agent through JFTech Open Platform AI detection workflows by clarifying the scenario, recommending supported no-database algorithms, invoking image or camera-snapshot analysis, and producing structured detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jftech](https://clawhub.ai/user/jftech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to select and call JFTech AI detection algorithms for authorized local images, image URLs, or camera snapshots. Typical scenarios include kitchen compliance, workplace safety, fire safety, perimeter security, retail inspection, vehicle management, and environmental monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores JFTech API credentials, including appSecret, in a local config.json file.

Mitigation: Keep config.json out of shared exports and repositories, restrict local file access, rotate exposed credentials, and remove the file when it is no longer needed.

Risk: The workflow may open or use paid JFTech platform algorithm capabilities.

Mitigation: Confirm account authorization, billing expectations, and selected algorithms before running open or call commands.

Risk: The optional camera capture branch can process sensitive camera or surveillance imagery.

Mitigation: Use the skill only for authorized devices and data, and confirm that image handling complies with applicable privacy, workplace, and security requirements.

Risk: The optional capture dependency may be installed from an unpinned remote source.

Mitigation: Prefer a trusted, reviewed release of the dependency, pin the retrieved source where possible, and inspect it before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-algo-detection)
- [JFTech publisher profile](https://clawhub.ai/user/jftech)
- [Algorithm reference](artifact/reference.md)
- [Optional camera capture dependency](https://clawhub.ai/jftech/jf-open-pro-capture)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON command outputs and summaries, structured Markdown detection reports, and optional annotated evidence image files for local image inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local config.json credentials, result_<appUuid>.json API responses, and optional evidence images; output depends on JFTech API responses and Pillow availability for image rendering.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
