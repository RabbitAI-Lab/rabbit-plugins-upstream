## Description: <br>
Fast version of ByteDance's Seedance 2.0 for generating videos from text prompts, reference media, or first and last frame inputs through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate short videos with Seedance 2.0 Fast through the dLazy CLI. It supports text-to-video, multimodal reference inputs, first/last frame workflows, selectable aspect ratios, durations, and asynchronous polling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local media paths provided to the CLI may be uploaded to dLazy for processing. <br>
Mitigation: Avoid submitting sensitive or unauthorized content, and review dLazy service terms before use. <br>
Risk: The dLazy API key can be stored locally in the CLI configuration. <br>
Mitigation: Use OS account protections, prefer per-invocation credentials when appropriate, and rotate or revoke the organization API key if exposure is suspected. <br>
Risk: Generated outputs are hosted by dLazy. <br>
Mitigation: Review generated media URLs and sharing practices before distributing outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast) <br>
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON responses containing generated media URLs or asynchronous task status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated media is hosted by dLazy; local media paths supplied to the CLI may be uploaded for processing.] <br>

## Skill Version(s): <br>
1.3.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
