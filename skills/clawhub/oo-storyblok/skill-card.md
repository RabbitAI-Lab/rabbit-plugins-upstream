## Description: <br>
Storyblok lets an agent search and read Storyblok spaces, stories, links, tags, datasources, and datasource entries through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and agents use this skill to inspect Storyblok content through OOMOL's Storyblok connector. It supports read-oriented content lookup and retrieval for Storyblok spaces, stories, links, tags, datasources, and datasource entries when the user has connected a Storyblok account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Storyblok content available to the connected OOMOL account. <br>
Mitigation: Install it only for accounts where agent-assisted read access is acceptable, and review the connected account's access before use. <br>
Risk: Future connector actions marked write or destructive could change or remove Storyblok data. <br>
Mitigation: Require confirmation of the exact payload and effect before write actions, and explicit approval before destructive actions. <br>
Risk: The skill depends on the OOMOL oo CLI, authentication, Storyblok connection status, and billing state. <br>
Mitigation: Use the documented recovery steps only after matching command failures, rather than repeating setup proactively. <br>


## Reference(s): <br>
- [ClawHub Storyblok skill page](https://clawhub.ai/oomol/skills/oo-storyblok) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Storyblok homepage](https://www.storyblok.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill tells the agent to inspect live action schemas before constructing JSON payloads and to treat the documented Storyblok actions as read-oriented unless future actions are explicitly tagged otherwise.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
