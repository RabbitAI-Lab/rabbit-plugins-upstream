## Description:

Generate and edit images, create or extend video from images, derive or shorten prompt suggestions, and look up seeds with Midjourney through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Midjourney generation, editing, prompt, seed, and image-to-video workflows through RunAPI while following the current CLI or SDK contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit paid RunAPI/Midjourney jobs and may upload local media when a selected operation requires it.

Mitigation: Confirm authentication, pricing, operation contract, and user intent before submission; upload only files needed for the requested workflow.

Risk: A changed CLI or API contract can make a request invalid or produce unexpected response variants.

Mitigation: Discover the installed command help and current API reference before building requests, and stop on unresolved contract mismatches.

Risk: Incomplete verification can miss missing, empty, or wrong-type image or video deliverables.

Mitigation: Validate the complete response, download every requested media result, and check each file is non-empty with the expected MIME type or family.

## Reference(s):

- [RunAPI Midjourney model overview](https://runapi.ai/models/midjourney)
- [RunAPI Midjourney documentation](https://runapi.ai/models/midjourney.md)
- [RunAPI Midjourney provider overview](https://runapi.ai/providers/midjourney.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI Midjourney SDK](https://github.com/runapi-ai/midjourney-sdk)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-midjourney)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell command blocks, JSON request and response handling, SDK code snippets, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image or video deliverables; non-media results should be preserved in the requested JSON, text, SRT, or VTT format.]

## Skill Version(s):

0.3.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
