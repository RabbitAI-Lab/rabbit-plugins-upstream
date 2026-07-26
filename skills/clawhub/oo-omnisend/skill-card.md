## Description: <br>
Omnisend helps agents work with Omnisend contact and segment data through the OOMOL-backed oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read Omnisend contacts and segments, create or update contacts, and manage contact tags through a connected OOMOL account. It is suited for Omnisend support, marketing operations, and workflow automation tasks that need schema-checked connector calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Omnisend contact data through the connected OOMOL account. <br>
Mitigation: Install only when the publisher is trusted and the connected Omnisend account is appropriate for the task. <br>
Risk: Write and destructive actions can update contacts or remove contact tags. <br>
Mitigation: Review the exact payload and intended effect with the user before approving contact updates, tag changes, or destructive operations. <br>


## Reference(s): <br>
- [ClawHub Omnisend skill page](https://clawhub.ai/oomol/skills/oo-omnisend) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Omnisend homepage](https://www.omnisend.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
