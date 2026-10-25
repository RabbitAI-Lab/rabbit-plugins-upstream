## Description:

Unofficial Go client for the Runway API, generated with oapi-codegen from Runway's OpenAPI document. Package runway (github.com/psyb0t/go-runway) has typed methods on runway.ClientWithResponses for all 49 paths of https://api.dev.runwayml.com, among them text, image and video to video, text to image, upscaling, text to speech, sound effects, voice dubbing, voices, avatars, realtime sessions, recipes, workflows, documents, uploads, task polling and cancelling, and organization credit balance and usage. Requests authenticate with a Bearer API key plus the X-Runway-Version header set to 2024-11-06, both set in one request editor. Use when Go code needs to call Runway's generation API, poll a Runway task, or already imports go-runway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Runway API calls into a Go project, including submitting generation requests, polling task status, and accessing organization resources. It provides setup instructions and typed Go examples for authentication, requests, and responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send prompts, images, and other submitted content to Runway and require an API key.

Mitigation: Keep the API key in RUNWAYML_API_SECRET; do not hardcode, commit, log, or print request headers, and review what content is sent.

Risk: Generation requests can spend organization credits, and resource operations can cancel or delete resources.

Mitigation: Confirm the intended resources and requested operation before execution; review estimated cost and limit destructive actions to resources the user named or the task created.

Risk: An unpinned Go dependency version may change between installs.

Mitigation: Consider pinning the go-runway module version used by the project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup guidance, typed Go examples, and request/response handling patterns; no runtime file output.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
