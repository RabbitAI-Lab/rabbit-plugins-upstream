## Description:

Maps a short mood or atmosphere description to matching art styles and the feeling words that triggered them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xixi048](https://clawhub.ai/user/xixi048)

### License/Terms of Use:

MIT

## Use Case:

Artists, designers, and image-generation users can turn a plain-language mood or atmosphere into art-direction vocabulary and style candidates. Use the candidates as creative references; final art direction remains with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online analysis can transmit the user's description, and image requests may consume credits; billing terms can change.

Mitigation: Use --offline with a valid cached dictionary for local-only analysis. Before online analysis or image requests, obtain the user's approval and check current billing terms.

Risk: A saved quota token can grant access to quota-backed requests.

Mitigation: Keep quota tokens private and avoid exposing them in shared logs or files.

## Reference(s):

- [API contract](artifact/references/api-contract.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Style candidates with names, concise definitions, matched feeling words, and optional scores]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidates are directional suggestions, not a definitive art judgment.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
