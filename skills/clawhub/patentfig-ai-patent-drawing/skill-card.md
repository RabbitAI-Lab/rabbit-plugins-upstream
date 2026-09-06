## Description:

Generates patent-office-compliant patent figures, vector drawings, enhanced images, and filing-ready raster exports through the PatentFig AI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toplocalai](https://clawhub.ai/user/toplocalai)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and patent-support teams use this skill to guide an agent through PatentFig AI API calls for generating patent line art, vectorizing existing drawings, enhancing images, and preparing filing-ready figure outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent prompts, drawings, or invention details may contain confidential, pre-filing, client, or export-controlled material that would be sent to PatentFig AI.

Mitigation: Confirm that the user is comfortable sending the material to PatentFig AI before making API calls, and avoid submitting confidential or restricted content unless the user's policy permits it.

Risk: The skill requires a PATENTFIG_API_KEY, which could be exposed if printed, hardcoded, or written to logs.

Mitigation: Read the key only from the environment, never hardcode it, and do not print or persist it in files or logs.

Risk: Generation and conversion endpoints consume PatentFig AI credits.

Mitigation: State the operation and credit cost, check available balance for batches, and get user confirmation immediately before each billable call.

Risk: Install sources may need reproducible supply-chain review in controlled environments.

Mitigation: Pin or review install sources before deployment when organizational policy requires reproducible or approved dependencies.

## Reference(s):

- [PatentFig AI homepage](https://patentfig.ai)
- [PatentFig AI docs](https://patentfig.ai/docs)
- [PatentFig AI OpenAPI spec](https://patentfig.ai/api/openapi.yaml)
- [PatentFig AI endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/toplocalai/skills/patentfig-ai-patent-drawing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with curl examples, API response summaries, returned file URLs, and SVG or JSON payload references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PATENTFIG_API_KEY. Credit-consuming API calls should disclose cost and get user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
