## Description: <br>
Helps agents plan, gate, and audit ChatCut talking-head and screen-recording video edits with layouts, themes, transitions, face framing, captions, preview approval, media QA, delivery packages, and feedback governance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Video creators, editors, and agent operators use this skill to turn ChatCut talking-head, livestream clip, and screen-recording work into a reviewable production workflow. It is most useful when an agent must preserve content truth, validate captions, require previews and export approval, and produce auditable delivery artifacts before any manual or live route continues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local personal configuration can contain private notes, paths, terms, or project-specific values. <br>
Mitigation: Keep ~/.config/majia-chatcut-koubo local and out of repositories, and do not store passwords, tokens, cookies, or OAuth secrets in local notes. <br>
Risk: The workflow intentionally blocks Traditional Chinese caption output under the current project policy. <br>
Mitigation: Change and review the project policy before expecting Traditional Chinese captions to pass release validation. <br>
Risk: Real ChatCut adapters, real media probing or rendering, and platform publishing are marked unverified by the artifact. <br>
Mitigation: Require current environment evidence, preview approval, export authorization, and manual review before any live route or publishing action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-chatcut-koubo) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [Operating manual](artifact/references/operating-manual.md) <br>
- [Captions and terminology](artifact/references/captions-terminology.md) <br>
- [Recovery guide](artifact/references/recovery.md) <br>
- [Contract baseline](artifact/docs/contract-baseline.md) <br>
- [Roadmap](artifact/docs/roadmap.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON schemas, Node.js validation scripts, configuration templates, and CLI commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces fail-closed review gates and local configuration guidance; it does not automatically export or publish media.] <br>

## Skill Version(s): <br>
1.4.0 (source: SKILL.md metadata, package.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
