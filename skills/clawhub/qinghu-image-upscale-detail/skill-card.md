## Description:

Qinghu AI image upscaling skill that uses a tiled enlargement workflow to make product, portrait, landscape, and archival images larger and clearer while aiming to preserve the original content and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare higher-resolution images for product presentation, portraits, scenery, old-photo restoration, or print workflows. The skill guides the agent through qhkit option lookup, cost estimation, submission, polling, and result delivery for one image at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node and qhkit locally before use.

Mitigation: Preinstall Node and @iqinghu/qhkit through an approved package-management path and verify qhkit before running workflow commands.

Risk: Images may be uploaded to an external Qinghu workflow service and may consume paid Qinghu credits.

Mitigation: Use only images the user is authorized to process, run qhkit workflow estimate before generate, and wait for user confirmation when credits will be consumed.

Risk: The workflow depends on API-token configuration and may persist credentials locally.

Mitigation: Use an approved secret mechanism such as QHKIT_TOKEN or a controlled config path, avoid exposing tokens in logs, and confirm configuration with redacted qhkit output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON workflow responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one image per submission; completed workflow status may return image URLs and actual Qinghu credit consumption.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
