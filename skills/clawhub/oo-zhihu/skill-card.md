## Description:

Zhihu lets an agent read, create, and update Zhihu data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zhihu through an OOMOL-connected account, including search, hot lists, public user content, collections, Zhida knowledge bases, PDF parsing, PPT generation, and Zhida chat completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from unaudited URLs.

Mitigation: Inspect the installer first or use a pinned, signed, or separately reviewed oo CLI installation path.

Risk: The skill has broad trigger scope and includes write actions that can change Zhihu or Zhida state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: Using the connector requires trusting OOMOL with a connected Zhihu account.

Mitigation: Use the skill only when the user trusts OOMOL and is comfortable connecting the target Zhihu account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zhihu)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zhihu](https://www.zhihu.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
