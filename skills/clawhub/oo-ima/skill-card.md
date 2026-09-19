## Description:

ima (ima.qq.com). Use this skill for ANY ima request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate ima through an OOMOL-connected account, including reading notes and knowledge bases, creating or appending notes, and importing URLs or files when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's fallback setup includes remote installer commands, and evidence.security marks this as suspicious.

Mitigation: Install the oo CLI only through a trusted, verified method; do not let an agent run installer commands automatically.

Risk: Several ima actions can change account data, including creating notes, adding notes to knowledge bases, importing URLs, and uploading files.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ima)
- [ima Homepage](https://ima.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue read actions directly; write actions require user confirmation of the payload and effect.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
