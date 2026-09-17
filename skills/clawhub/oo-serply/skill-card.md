## Description:

Serply lets agents search and read Google web, News, Scholar, and Video results through an OOMOL-connected Serply account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Serply-backed Google web, News, Scholar, and Video searches through the oo CLI and receive structured search results. It is suited for search and retrieval workflows where the user has already connected Serply through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could execute unreviewed code.

Mitigation: Do not allow an agent to run the curl-to-bash or PowerShell iex installer automatically; install the oo CLI through a verified method after reviewing what it changes.

Risk: Search queries and connector activity may be processed by third-party services.

Mitigation: Use the skill only when the user trusts OOMOL and Serply for the searches being requested.

## Reference(s):

- [Serply homepage](https://serply.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector response includes data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
