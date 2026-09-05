## Description:

Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the user needs to navigate websites, interact with web pages, fill forms, take screenshots, test web applications, or extract information from web pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[platonai](https://clawhub.ai/user/platonai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to direct an agent through browser navigation, interaction, screenshots, web testing, and structured data extraction with browser4-cli. It is intended for browser workflows that need Chrome or Chromium control through command-line guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant broad browser-control authority over live browser sessions and saved login state.

Mitigation: Use dedicated test browser profiles and test accounts, and avoid attaching to personal or production sessions.

Risk: HAR captures, browser state files, imported profiles, and extension tokens may contain sensitive data.

Mitigation: Treat those files and tokens as secrets, store them in controlled locations, and avoid sharing them unless they have been reviewed and sanitized.

Risk: Background crawl, swarm, loop, LLM-backed agent actions, and skill-management commands may perform broad or repeated actions.

Mitigation: Review the command scope, target sites, credentials, and side effects before running these workflows.

Risk: Full browser profile import can expose more personal or production data than a task requires.

Mitigation: Prefer narrow state-save and state-load workflows, and import full profiles only when necessary.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/platonai/Browser4/tree/main/skills/browser4-cli)
- [ClawHub skill page](https://clawhub.ai/platonai/skills/browser4-cli)
- [Browser4 CLI skill instructions](artifact/SKILL.md)
- [Quick reference](artifact/references/quickstart.md)
- [Snapshot reference](artifact/references/snapshot.md)
- [HTML snapshot reference](artifact/references/htmlsnapshot.md)
- [Crawl command reference](artifact/references/crawl.md)
- [Swarm reference](artifact/references/swarm.md)
- [Agent execution reference](artifact/references/agent.md)
- [Browser state import reference](artifact/references/browser-state-import.md)
- [Network inspection reference](artifact/references/network.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide browser automation commands that produce text, JSON, screenshots, HAR files, browser state files, or extracted datasets.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
