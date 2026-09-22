## Description:

Generates podcast chapters, highlights, and show notes from podcast audio or transcripts, with Chinese interaction and configurable text, Markdown, or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast creators, editors, developers, and automation teams use this skill to turn podcast audio or transcripts into chapters, highlights, and show notes for publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and command execution capability for a loosely scoped media workflow.

Mitigation: Run it only in a constrained workspace containing podcast files intended for processing, and review requested file or command actions before allowing them.

Risk: The artifact describes command whitelist protections that may not be enforced by the runtime platform.

Mitigation: Do not rely on the claimed whitelist unless the platform independently enforces it; use sandboxing and least-privilege permissions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, or plain text, depending on the requested mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated chapters, highlights, show notes, processing status, and metadata.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
