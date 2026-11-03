## Description:

Creates a complete picture book from a theme, with a paged story, consistent illustrations, matching background music, and a self-contained HTML reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users who want a children's book or bedtime story can turn a theme into a paged narrative, illustrated scenes, optional background music, and an HTML book they can read and share.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation requests may incur charges, and prompts or reference images are uploaded to dLazy services.

Mitigation: Confirm the user expects paid generation, and avoid uploading sensitive prompts or images unless they are authorized for that use.

Risk: Externally supplied image paths in book data can inject browser code into the generated HTML.

Mitigation: Use a dedicated output folder and agent-created book.json with fixed local media paths; review asset paths before building the book.

Risk: The external CLI package was not fully audited, and its credential-storage protections were not independently verified.

Mitigation: Protect the API key, use a trusted and reviewed CLI installation, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [CLI project reference](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)

## Skill Output:

**Output Type(s):** [HTML, JSON, Text, Images, Audio]

**Output Format:** [A self-contained HTML picture book with a book.json source, illustrations, and optional MP3 background music.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; includes page navigation and a responsive reading layout, with optional looping background music.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
