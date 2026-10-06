## Description:

Prepares support intake digests and builds follow-up case comments from supplied support information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams use supplied intake messages to prepare structured case digests and follow-up comments. The downstream operation can save a local case artifact when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream case artifact may retain support information on the local filesystem.

Mitigation: Use a dedicated output directory and avoid supplying sensitive support snippets unless appropriate for the workflow.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON objects for the digest or case comment; a local JSON file for the downstream case artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation requires a writable output directory and does not update an external support service.]

## Skill Version(s):

3.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
