## Description:

Analyzes short-video links to derive a script and help recreate the style, rhythm, and shot structure for marketing videos using the user's product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers and content creators use this skill to analyze Douyin or TikTok viral video links, rewrite the derived script for their own product, and generate comparable LinkPix/qhkit marketing videos after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require qhkit API key configuration, and the security evidence warns against pasting API keys into normal chat.

Mitigation: Use a secure secrets mechanism or environment variable outside the conversation when available, and avoid exposing raw tokens in chat.

Risk: The skill performs local qhkit installation or upgrade steps and may install Node locally.

Mitigation: Review installation commands before execution, prefer official registries, and keep SHA256 verification before unpacking Node downloads.

Risk: The workflow uploads user media to the LinkPix/qhkit service and may consume paid credits for generation.

Mitigation: Use only media the user is authorized to process, run estimates where supported, and confirm the generation parameters and credit cost before paid task submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten scripts, status checks, generated media URLs, and credit estimates from qhkit task responses.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
