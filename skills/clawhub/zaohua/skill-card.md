## Description: <br>
Creates local fictional AI Soul packages from natural-language or guided input, supports synthetic previews and live trial chat, and evaluates local packages with SOUL-6 while avoiding real-person cloning or impersonation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fooying](https://clawhub.ai/user/fooying) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent users use this skill to create original fictional AI persona packages, preview or trial their behavior, and run a local SOUL-6 quality assessment before sharing or importing the package. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be auto-selected for AI personality or companion requests. <br>
Mitigation: Use it for fictional, original AI Soul creation and avoid requests to clone, distill, or impersonate real people or public figures. <br>
Risk: Generated packages can contain locally written runtime files, reports, audition artifacts, and optional ZIP archives. <br>
Mitigation: Review generated package contents and SOUL-6 results before sharing, publishing, or importing them into another agent host. <br>
Risk: Live trial chat can make a generated Soul feel persistent or personal even though trial messages are temporary. <br>
Mitigation: Keep trial chat separate from canon and memory, and preserve the skill's boundaries around emotional dependency, professional advice, and severe distress. <br>


## Reference(s): <br>
- [Generate Workflow](artifact/references/create-workflow.md) <br>
- [AI Soul Package Contract](artifact/references/package-contract.md) <br>
- [SOUL-6 v1.0](artifact/references/soul-6.md) <br>
- [Source Safety and Local-Only Operation](artifact/references/source-safety.md) <br>
- [Preview, Trial Chat, and Behavioral Evaluation](artifact/references/try-chat.md) <br>
- [SOUL-6 Review Metrics](https://aisoulhub.io/about/review-metrics#soul6) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and local package files, with optional JSON reports and ZIP archives] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates files under a workspace output directory and keeps trial chats, auditions, and reports separate from runtime memory and canon.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
