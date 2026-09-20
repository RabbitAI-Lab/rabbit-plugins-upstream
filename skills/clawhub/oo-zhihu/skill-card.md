## Description:

Zhihu (zhihu.com) lets agents read, create, and update Zhihu data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zhihu through an OOMOL-connected account, including search, hot-list discovery, public content lookup, collections, Zhida knowledge-base workflows, PDF parsing, and PPTX generation. The skill instructs agents to inspect live connector schemas before running actions and to confirm payloads before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may lead users to pipe a remote oo CLI installer script directly into a shell without verification.

Mitigation: Review the installer before running it, prefer a signed or checksummed release or package-manager install, and manually inspect scripts when possible.

Risk: Write actions can change Zhihu or Zhida account state if an agent submits the wrong payload or targets the wrong account.

Mitigation: Fetch the live connector schema first and confirm the exact payload, intended effect, and target account before running write actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zhihu](https://www.zhihu.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require confirmation of payload and target account.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
