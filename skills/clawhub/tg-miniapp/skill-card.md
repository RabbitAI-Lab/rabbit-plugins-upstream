## Description: <br>
Builds and debugs Telegram Mini Apps with guidance for safe areas, fullscreen mode, BackButton handlers, inline sharing, position:fixed issues, WebApp API behavior, and React gotchas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenith2828](https://clawhub.ai/user/zenith2828) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to build and debug Telegram Mini Apps, especially safe area handling, fullscreen layouts, BackButton handlers, sharing with inline mode, fixed-position UI, and React rendering pitfalls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sharing examples may be connected to real bot or user data before review. <br>
Mitigation: Review the sharing flow before connecting production bot or user data, and prepare a fresh prepared_message_id for each share attempt. <br>
Risk: Debug diagnostics could be visible in production if the DebugOverlay is deliberately enabled. <br>
Mitigation: Keep DebugOverlay disabled in production unless exposing diagnostics is an intentional release decision. <br>
Risk: Copied guidance or components may behave differently across Telegram launch paths and mobile platforms. <br>
Mitigation: Run the included checklist across folder launch, direct bot chat, iOS, Android, sharing, BackButton, and sticky-header scrolling before release. <br>


## Reference(s): <br>
- [Telegram Mini App Knowledge Base](references/KNOWLEDGE.md) <br>
- [Telegram Mini App React Hooks](references/hooks.ts) <br>
- [Telegram Mini App React Components](references/components.tsx) <br>
- [ClawHub Skill Page](https://clawhub.ai/zenith2828/skills/tg-miniapp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript and TSX code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes copy-paste React hooks and components plus a Telegram Mini App testing checklist.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
