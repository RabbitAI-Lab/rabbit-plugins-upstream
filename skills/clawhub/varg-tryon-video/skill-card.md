## Description:

Creates apparel try-on videos from garment and model images, with fit-check motion and size disclosures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion and apparel sellers use this skill to create try-on ads from flat-lay or product photos, showing fit-check movements and labeling the model and size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: People may upload real-person photos without understanding the service's privacy limits.

Mitigation: Use generated or consenting subjects, explain the service's privacy limits, and review Varg's privacy terms before processing real-person images.

Risk: Image URLs may expose credentials, and video generation may incur unplanned usage costs.

Mitigation: Avoid URLs containing credentials and agree on a generation budget before running the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/varg-tryon-video)
- [VARG how-to](https://varg.ai/how-to)
- [VARG MCP connection](https://mcp.varg.ai/mcp)
- [Try-on model test notes](https://suzuki-shoten.pages.dev/blog/metafit-genai-part2)
- [Tested video example](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_1213e32adbda.mp4)

## Skill Output:

**Output Type(s):** [Video, Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Try-on video clips and a captioned ad, with Markdown workflow guidance and inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically combines 3–4 short clips into a 15-second ad; includes size-caption and AI-model disclosure guidance.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
