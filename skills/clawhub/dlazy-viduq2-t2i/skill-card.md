## Description:

Generate high-quality images with Vidu Q2 using text-to-image or image-to-image prompts through the dLazy cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Vidu Q2 images from text prompts or optional reference images. It is intended for normal dLazy cloud image-generation workflows that require a dLazy API key and available account credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image inputs may be uploaded to dLazy cloud endpoints for inference.

Mitigation: Use the skill only for intended dLazy requests and avoid passing sensitive prompts or local files.

Risk: Generated outputs are hosted by dLazy and returned as remote file URLs.

Mitigation: Review output URLs and downloaded files before sharing or reusing them in downstream workflows.

Risk: A saved dLazy API key remains on the local machine until removed or revoked.

Mitigation: Prefer least-privilege operational practices, rotate or revoke keys when needed, and remove local credentials on shared machines.

Risk: Cloud generation may consume paid account credits.

Mitigation: Use dry-run or cost-estimate behavior where available and confirm account balance before large generation runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Files, Guidance]

**Output Format:** [JSON responses with image URLs, optional downloaded image files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, account-balance errors, API-key authentication, and optional local file upload for image inputs.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
