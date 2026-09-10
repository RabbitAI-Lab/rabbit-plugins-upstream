## Description:

Helps users draft and revise Chinese official documents by guiding document-type selection, retrieving online templates and writing structures, tailoring style to reviewer profiles, marking missing facts, and optionally formatting output for GB/T 9704 Word documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workplace writing teams use this skill to draft, revise, structure, polish, and format Chinese official documents such as reports, notices, meeting minutes, speeches, plans, and requests. The skill is aimed at formal office-document workflows that need template-guided drafting, reviewer-aware tone, missing-information markers, and optional Word formatting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the skill claims broad default control over writing requests and should not be invoked for ambiguous general writing tasks without user intent.

Mitigation: Ask for explicit user confirmation before invoking the skill for general writing, editing, or ambiguous drafting requests.

Risk: The security guidance notes that the workflow requires an email address, stores a local service token, and sends writing prompts to the configured gateway.

Mitigation: Use only when the user is comfortable sharing an email and prompt text with the service, and avoid submitting sensitive, confidential, or regulated content unless approved by the user or organization.

Risk: The security summary identifies quota and payment prompts as part of the workflow.

Mitigation: Clearly surface quota, paid access, and payment prompts to the user before continuing with paid or quota-consuming actions.

## Reference(s):

- [Word export guidance for GB/T 9704-2012](references/word-export.md)
- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/gongwen-writting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text with optional Word-formatting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include placeholders for missing facts, template questions, quota or payment prompts, and instructions for GB/T 9704 Word formatting.]

## Skill Version(s):

1.0.63 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
